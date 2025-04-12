# REMOVE SPECIAL CHARACTERS
def remove_special_characters(lyrics):
    try:
        removed_characters="".join(ch for ch in lyrics if ch.isalnum())
    except Exception as e:


# REPLACE WORDS WITH IRISH ONES

# ADD FIXES FOR PRONOUNCIATION