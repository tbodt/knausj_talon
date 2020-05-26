from talon import Module, Context
from talon.grammar import Phrase

mod = Module()

@mod.capture(rule='({user.vocabulary} | <word>)')
def word(m) -> str:
    try: word = m.vocabulary
    except AttributeError: word = m.word
    return Phrase._new_phrase([word])

@mod.capture(rule='({user.vocabulary} | <phrase>)+')
def phrase(m) -> str:
    words = []
    try: vocab_list = m.vocabulary_list
    except AttributeError: vocab_list = []
    for token in m:
        if isinstance(token, Phrase):
            words.extend(token._words)
        else:
            words.append(vocab_list.pop(0))
    return Phrase._new_phrase(words)

mod.list('vocabulary', desc='user vocabulary')
