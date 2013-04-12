import pytest
import filespy


@pytest.fixture
def s_empty():
    return {}


@pytest.fixture
def s1():
    return {
        'one': 1
    }


@pytest.fixture
def s_multi1():
    return {
        'one': 1,
        'two': 2,
        'three': 3
    }


@pytest.fixture
def s_multi2():
    return {
        'one': 1,
        'two': -2,
        'four': 4
    }


def test_empty(s_empty):
    assert list(filespy.snapshot_diff(s_empty, s_empty.copy())) == []


def test_empty_one(s_empty, s1):
    i = list(filespy.snapshot_diff(s_empty, s1))
    assert i == [
        (filespy.CREATED, 'one'),
    ]


def test_one_empty(s1, s_empty):
    i = list(filespy.snapshot_diff(s1, s_empty))
    assert i == [
        (filespy.DELETED, 'one'),
    ]


def test_empty_multi(s_empty, s_multi1):
    i = sorted(filespy.snapshot_diff(s_empty, s_multi1))
    assert i == [
        (filespy.CREATED, 'one'),
        (filespy.CREATED, 'three'),
        (filespy.CREATED, 'two'),
    ]


def test_multi_empty(s_multi1, s_empty):
    i = sorted(filespy.snapshot_diff(s_multi1, s_empty))
    assert i == [
        (filespy.DELETED, 'one'),
        (filespy.DELETED, 'three'),
        (filespy.DELETED, 'two'),
    ]


def test_multi_multi(s_multi1, s_multi2):
    i = sorted(filespy.snapshot_diff(s_multi1, s_multi2))
    assert i == [
        (filespy.CREATED, 'four'),
        (filespy.DELETED, 'three'),
        (filespy.MODIFIED, 'two'),
    ]
