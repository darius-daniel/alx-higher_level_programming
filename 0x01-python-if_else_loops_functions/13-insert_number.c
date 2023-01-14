#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: integer
 *
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (number > current->n && current->next != NULL)
		{
			prev = current;
			current = current->next;
		}

		if (prev == NULL)
		{
			new->next = *head;
			*head = new;
		}
		else if (current->next == NULL)
			current->next = new;
		else
		{
			prev->next = new;
			new->next = current;
		}
	}
	return (new);
}
