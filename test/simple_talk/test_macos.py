import platform
from pathlib import Path
from typing import cast
from uuid import uuid4

import pytest
from moviepy.audio.io.AudioFileClip import AudioFileClip

from simple_talk import SimpleTalk

macos_only = pytest.mark.skipif(
    platform.system() != "Darwin",
    reason="Need to use macOS's builtin synthesizer",
)

TEXT = "Hello there! My name is Bob."


@macos_only
def test_simple_talk() -> None:
    t = SimpleTalk()

    clip: AudioFileClip = cast("AudioFileClip", t.talk(TEXT))
    assert isinstance(clip, AudioFileClip)
    assert clip.duration > 1
    path = Path(clip.filename)
    assert path.suffix == ".mp3"
    path.unlink()

    filename_prefix = str(uuid4())
    filename: str = cast("str", t.talk(TEXT, filename_prefix))
    path = Path(filename)
    assert path.suffix == ".mp3"
    path.unlink()


@macos_only
def test_simple_talk_no_normalize_volume() -> None:
    t = SimpleTalk(normalize_volume=False)

    filename_prefix = str(uuid4())
    filename: str = cast("str", t.talk(TEXT, filename_prefix))
    path = Path(filename)
    assert path.suffix == ".mp4"
    path.unlink()


@macos_only
def test_simple_talk_by_sentence() -> None:
    t = SimpleTalk()

    filenames = t.talk_by_sentence(TEXT)
    assert len(filenames) == 1
    assert filenames[0][0] == TEXT

    clip: AudioFileClip = cast("AudioFileClip", filenames[0][1])
    assert isinstance(clip, AudioFileClip)
    assert clip.duration > 1
    path = Path(clip.filename)
    assert path.suffix == ".mp3"
    path.unlink()

    filename_prefix = str(uuid4())
    filenames = t.talk_by_sentence(TEXT, filename_prefix)
    filename: str = cast("str", filenames[0][1])
    path = Path(filename)
    assert path.suffix == ".mp3"
    path.unlink()
