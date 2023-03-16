/**
 * delete_dnodeint_at_index - deletes a node at a given index
 * @head: double pointer to head of list
 * @index: index of node to be deleted
 *
 * Return: 1 if succeeded, -1 if failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current_node, *previous_node;
	unsigned int i;

	if (*head == NULL) /* check if list is empty */
		return (-1);
	
	current_node = *head;
	if (index == 0) /* delete head node */
	{
		*head = current_node->next;
		if (*head)
			(*head)->prev = NULL;
		free(current_node);
		return (1);
	}
	
	for (i = 0; i < index; i++)
	{
		previous_node = current_node;
		current_node = current_node->next;
		if (current_node == NULL) /* index out of range */
			return (-1);
	}
	previous_node->next = current_node->next; /* delete node */
	if (current_node->next)
        current_node->next->prev = previous_node;
	free(current_node);
    return (1);
}

