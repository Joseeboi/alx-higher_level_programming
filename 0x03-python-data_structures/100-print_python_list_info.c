#include <python.h>

void print_python_list_info(pyObject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = py_SIZE(p);
	alloc = ((pylistobject *)p)->allocated;

	printf("[*] size of the python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = pyList_GetItem(p, i);
		printf("%s\n", py_TYPE(obj)->tp_name);
	}
}