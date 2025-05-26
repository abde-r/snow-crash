#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

int main(int ac, char **av) {
	(void)ac;
	size_t  len = strlen(av[1]);
	for (int i = 0; i < len; ++i)
    	{
        	uint8_t c = av[1][i] - i;
        	write(STDOUT_FILENO, &c, 1);
    	}
    	write(STDOUT_FILENO, "\n", 1);
    	return 0;
}
