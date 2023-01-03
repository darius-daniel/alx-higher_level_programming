#include "lists.h"

int check_cycle(listint_t *list)
{
	int result = 0;

	while (list != NULL)
	{
		if (list->passed_here == 1)
		{
			result =  1;
			break;
		}
		list->passed_here = 1;
		list = list->next;
	}

	if (result == 1)
	{
		while (list != NULL && list->passed_here != 0 )
		{
			list->passed_here = 0;
			list = list->next;
		}
	}

	return (result);
}