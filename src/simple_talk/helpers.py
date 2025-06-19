from textstat import syllable_count

# https://www.researchgate.net/publication/235971274_A_cross-Language_Perspective_on_Speech_Information_Rate
ENGLISH_AVERAGE_SYLLABLES_PER_SECOND = 6.19


def estimate_speech_duration(text: str) -> float:
    return syllable_count(text) / ENGLISH_AVERAGE_SYLLABLES_PER_SECOND
