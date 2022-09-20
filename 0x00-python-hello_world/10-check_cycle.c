#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Check for cycle
  * @list: argument
  *
  * Return: 1 if has a cycle positive or 0 if none
  */	
int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;
	int positive = 0;

	while ((a && b) && b->next)
	{		
		a = a->next;

		if (b->next || b->next->next)	
			b = b->next->next;
		else
			break;

		if (a == b)
		{
			positive = 1;
			break;
		}
	}

	return (positive);
}
	
