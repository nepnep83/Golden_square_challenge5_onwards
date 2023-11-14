from lib.diary_entry import *

"""
Test that 2 arguments are passed into __init__()
"""
def test_init_receives_2_args():
    #check type error is thrown
    pass


"""
Test with correct inputs, returns correctly formatted diary entry
"""
def test_format_with_correct_args():
    #check output is formatted correctly
    diary = DiaryEntry("Day 1", "Today I went to the park")
    result = diary.format()
    assert result == "Day 1: Today I went to the park"


"""
Check that the correct word count is returned
"""
def test_correct_word_count_is_returned():
    diary = DiaryEntry("Day 1", "Today I went to the park")
    assert diary.count_words() == 8


"""
Check that no error is thrown when inputs are empty for count_words()
"""
def test_no_error_when_inputs_are_empty_in_count_words():
    diary = DiaryEntry("", "")
    assert diary.count_words() == 0


"""
Check that the output is an int
"""
def test_output_is_int():
    diary = DiaryEntry("Day 1", "Today I went to the park")
    assert type(diary.count_words()) == int


"""
Check that correct time estimate is returned fo reading_time()
"""
def test_check_correct_time_est():
    diary = DiaryEntry('hello', 'hello '*99)
    result = diary.reading_time(100)
    assert result == 1

"""
Check that estimated time is rounded correctly
"""

"""
check that the output is an int
"""

"""
Check that error is thrown when WPM is <= 0
"""

"""
Check all contents is read in the time given
"""

"""
Check that calling function for a second time does not return you to the start of the contents,
but where you left off
"""

"""
Check that no error is returned when not enough words are present in the contents
"""

"""
Check that once all text is read, once called again, the user starts from the beginning.
"""

"""
Check that error is thrown when WPM is <= 0
"""

"""
Check that no error is thrown when minutes <= 0 
"""