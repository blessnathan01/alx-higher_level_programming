#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size, x;
	PyListObject *list;
	PyObject *element;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < size; x++)
	{
		element = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
