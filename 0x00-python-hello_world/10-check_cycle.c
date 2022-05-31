#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle or not
 * @list: pointer to the list
 *
 * Return: 1 if a cycle is present
 * and 0 when a cycle is absent
 */
int check_cycle(listint_t *list)
{
	listint_t *_nxt;
	listint_t *prev;

	_nxt = list;
	prev = list;
	while (list && _nxt && _nxt->next)
	{
		list = list->next;
		_nxt = _nxt->next->next;

		if (list == _nxt)
		{
			list = prev;
			prev = _nxt;
			while (1)
			{
				_nxt = prev;
				while (_nxt->next != list && _nxt->next != prev)
				{
					_nxt = _nxt->next;
				}
				if (_nxt->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
