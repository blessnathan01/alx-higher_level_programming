#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: double pointer to list.
  *
  *Return: 1 if palindrome, 0 if not palindrom.
  */
int is_palindrome(listint_t **head)
{
	return (checkPalindrome(head, *head));
}

/**
  * checkPalindrome - recursive function ot check if sinly linked list
  * is a palindrome.
  * @headptr: double pointer to list.
  * @cptr: pointer to list.
  *
  * Return: 1 or 0
  */
int checkPalindrome(listint_t **headptr, listint_t *cptr)
{
	int response;

	if (cptr == NULL)
		return (1);
	response = checkPalindrome(headptr, cptr->next) && ((*headptr)->n == cptr->n);
	return (response);
}
