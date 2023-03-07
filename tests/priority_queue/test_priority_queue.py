from ting_file_management.priority_queue import PriorityQueue
import pytest

files_list = [
    {
            'nome_do_arquivo': 'teste1.txt',
            'qtd_linhas': 4,
            'linhas_do_arquivo': [
                'linha',
                'linha',
                'linha',
                'linha',
            ],
    },
    {
            'nome_do_arquivo': 'teste1.txt',
            'qtd_linhas': 2,
            'linhas_do_arquivo': [
                'linha',
                'linha',
            ],
    },
    {
            'nome_do_arquivo': 'teste1.txt',
            'qtd_linhas': 5,
            'linhas_do_arquivo': [
                'linha',
                'linha',
                'linha',
                'linha',
                'linha',
            ],
    },
]


def test_basic_priority_queueing():
    priority = PriorityQueue()

    for item in files_list:
        priority.enqueue(item)

    with pytest.raises(IndexError):
        priority.search(5)

    assert len(priority.regular_priority) == 1
    assert len(priority.high_priority) == 2
    assert priority.is_priority(files_list[0]) is True
    assert priority.is_priority(files_list[2]) is False
    assert priority.search(2) == files_list[2]
    assert priority.dequeue() == files_list[0]
