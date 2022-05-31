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
	listint_t *nxt;
	listint_t *prev;

	nxt = list;
	prev = list;
	while (list && nxt && nxt->next)
	{
		list = list->next;
		nxt = nxt->next->next;

		if (list == nxt)
		{
			list = prev;
			prev = nxt;
			while (1)
			{
				nxt = prev;
				while (nxt->next != list && nxt->next != prev)
				{
					nxt = nxt->next;
				}
				if (nxt->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
