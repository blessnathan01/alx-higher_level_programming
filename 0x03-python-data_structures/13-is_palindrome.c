#include "lists.h"

/**
 * rev - reverses the second half of the list
 *
 * @h_rev: head of the second half
 * Return: nothing
 */
void rev(listint_t **h_rev)
{
	listint_t *p;
	listint_t *c;
	listint_t *n;

	prv = NULL;
	crr = *h_rev;

	while (c != NULL)
	{
		n = c->next;
		c->next = p;
		p = c;
		c = n;
	}

	*h_rev = p;
}

/**
 * cmp - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int cmp(listint_t *h1, listint_t *h2)
{
	listint_t *tmpA;
	listint_t *tmpB;

	tmpA = h1;
	tmpB = h2;

	while (tmpA != NULL && tmpB != NULL)
	{
		if (tmpA->n == tmpB->n)
		{
			tmpA = tmpA->next;
			tmpB = tmpB->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmpA == NULL && tmpB == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly list is
 * a palindrome
 * @head: pointer of the pointer
 *
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		rev(&scn_half);
		isp = cmp(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
