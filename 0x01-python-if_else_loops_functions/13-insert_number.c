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
  listint_t *current;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
	  return (NULL);

  new->n = number;
  new->next = NULL;

  current = *head;
  if (current == NULL)
  {
    new->next = *head;
    *head = new;
  }
  else
    {
    while (current->next != NULL && current->next->n < number)
      current = current->next;

    new->next = current->next;
    current->next = new;
  }
  return (new);
}
