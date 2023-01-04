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
  listint_t *prev;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
	  return (NULL);

  new->n = number;
  new->next = NULL;

  if (*head == NULL)
  {
    new->next = NULL;
    *head = new;
  }
  else
  {
    current = *head;
    while (current->next != NULL && current->n < number)
    {
      prev = current;
      current = current->next;
    }

    prev->next = new;
    new->next = current;
  }
  return (new);
}
