#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
  int *int_arr = to_int_array(*head);
  unsigned int n = 0, size = count_nodes(*head);
  unsigned int last_int = size - 1;
  int result = 1;

  while (n < size / 2)
  {
    if (int_arr[n] == int_arr[last_int])
    {
      n++, last_int--;
      continue;
    }
    result = 0;
    break;
  }

  free(int_arr);
  return (result);
}

/**
 * to_int_array - collects the contents of a linked list into an array.
 * @head: pointer to the first node of the linked list.
 *
 * Return: a pointer to the first element of the dynamically allocated array.
 */
int *to_int_array(listint_t *head)
{
  unsigned int i = 0, n_nodes = count_nodes(head);
  int *int_array;
  listint_t *current = head;

  int_array = (int *)malloc(sizeof(int) * n_nodes);
  if (int_array == NULL)
  {
    fprintf(stderr, "error: %s\n", strerror(errno));
    exit(EXIT_SUCCESS);
  }

  while (i < n_nodes)
  {
    int_array[i] = current->n;
    current = current->next;
    i++;
  }

  return (int_array);
}


/**
 * count_node = counts the number of nodes in a linked list
 * @h: pointer to the first node in the linked list
 * Return: the total number of nodes in the linked list
 */
unsigned int count_nodes(listint_t *h)
{
  size_t n = 0;
  listint_t *current = h;

  while (current != NULL)
  {
    n++;
    current = current->next;
  }

  return (n);
}
