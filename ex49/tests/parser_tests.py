from nose.tools import *
from ex48 import parser


def sentence_tests():
    sentence = parser.Sentence(('number', 1), ('subject', 'asubject'), ('verb', 'averb'), ('object', 'aobject'))
    assert_equals(sentence.num_subjects, 1)
    assert_equals(sentence.subject, 'asubject')
    assert_equals(sentence.verb, 'averb')
    assert_equals(sentence.object, 'aobject')


def peek_tests():
    word_list = [('type_a', 'word_a'), ('type_b', 'word_b')]
    assert_equals(parser.peek(word_list), 'type_a')

    word_list = [('type_b', 'word_b')]
    assert_equals(parser.peek(word_list), 'type_b')

    word_list = []
    assert_equals(parser.peek(word_list), None)


def match_tests():
    word_list = [('type_a', 'word_a'), ('type_b', 'word_b')]
    assert_equals(parser.match(word_list, 'type_a'), ('type_a', 'word_a'))
    assert_equals(parser.match(word_list, 'type_b'), ('type_b', 'word_b'))
    assert_equals(parser.match(word_list, 'type_c'), None)


def parse_skip_tests():
    word_list = [('type_a', 'word_a'), ('type_a', 'word_a'), ('type_b', 'word_b')]
    parser.skip(word_list, 'type_a')
    assert_equals(parser.peek(word_list), 'type_b')
    parser.skip(word_list, 'type_b')
    assert_equals(parser.peek(word_list), None)

def parse_number_tests():
    word_list = [('number', 10), ('noun', 'heads')]
    assert_equals(parser.parse_number(word_list), ('number', 10))
    assert_equals(parser.parse_number(word_list), ('number', 0))


def parse_verb_tests():
    word_list = [('stop', 'stop_a'), ('verb', 'verb_a'), ('noun', 'noun_a')]
    assert_equals(parser.parse_verb(word_list), ('verb', 'verb_a'))
    assert_raises(parser.ParserError, parser.parse_verb, word_list)
    assert_equals(word_list, [('noun', 'noun_a')])


def parse_object_tests():
    word_list = [('stop', 'stop_a'), ('verb', 'verb_a'), ('noun', 'noun_a'), ('direction', 'direction_a')]
    assert_raises(parser.ParserError, parser.parse_object, word_list)
    parser.parse_verb(word_list)
    assert_equals(word_list, [('noun', 'noun_a'), ('direction', 'direction_a')])
    assert_equals(parser.parse_object(word_list), ('noun', 'noun_a'))
    assert_equals(parser.parse_object(word_list), ('direction', 'direction_a'))


def parse_subject_tests():
    word_list = [('verb', 'eat'), ('stop', 'the'), ('noun', 'bear')]
    sentence = parser.parse_subject(word_list, ('number', 0), ('noun', 'The Subject'))
    assert_equals(sentence.num_subjects, 0)
    assert_equals(sentence.subject, 'The Subject')
    assert_equals(sentence.verb, 'eat')
    assert_equals(sentence.object, 'bear')

    word_list = [('verb', 'ate'), ('stop', 'the'), ('noun', 'zebra')]
    sentence = parser.parse_subject(word_list, ('number', 10), ('noun', 'lions'))
    assert_equals(sentence.num_subjects, 10)
    assert_equals(sentence.subject, 'lions')
    assert_equals(sentence.verb, 'ate')
    assert_equals(sentence.object, 'zebra')

    word_list = [('noun', 'bee'), ('verb', 'stung'), ('stop', 'the'), ('noun', 'human')]
    # in real usage, first tuple should have matched/been popped already
    assert_raises(parser.ParserError, parser.parse_subject, word_list, ('number', 0), ('noun', 'bee'))
    word_list = [('verb', 'stung'), ('stop', 'the'), ('adj', 'freaking'), ('noun', 'human')]
    # extra in front of the object
    assert_raises(parser.ParserError, parser.parse_subject, word_list, ('number', 0), ('noun', 'bee'))


def parse_sentence_tests():
    word_list = [('stop', 'the'), ('adj', 'damned'), ('noun', 'bee'), ('verb', 'stung'), ('stop', 'the'), ('noun', 'human')]
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)

    word_list = [('number', 10), ('noun', 'lions'), ('verb', 'ate'), ('stop', 'the'), ('noun', 'zebra')]
    sentence = parser.parse_sentence(word_list)
    assert_equals(sentence.num_subjects, 10)
    assert_equals(sentence.subject, 'lions')
    assert_equals(sentence.verb, 'ate')
    assert_equals(sentence.object, 'zebra')

    word_list = [('stop', 'the'), ('noun', 'bee'), ('verb', 'stung'), ('stop', 'the'), ('noun', 'human')]
    sentence = parser.parse_sentence(word_list)
    assert_equals(sentence.subject, 'bee')
    assert_equals(sentence.verb, 'stung')
    assert_equals(sentence.object, 'human')

    word_list = [('verb', 'stung'), ('stop', 'the'), ('noun', 'human')]
    sentence = parser.parse_sentence(word_list)
    assert_equals(sentence.subject, 'player')
    assert_equals(sentence.verb, 'stung')
    assert_equals(sentence.object, 'human')

    word_list = [('start', 'hello'), ('noun', 'bee'), ('verb', 'stung'), ('stop', 'the'), ('noun', 'human')]
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)
