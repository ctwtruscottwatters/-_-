// Basic Vulnerability
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <Windows.h>
int main(void)
{
	SetProcessDEPPolicy(1);
	FILE* fp;
	unsigned char buffer[128];
	/* unsigned char address[] = "\xfe\xfe\xf0\xf0"; */
	unsigned char shellcode[] = "\x90\x90\x90\x90\x90\x90\x90\x90\xCC\xCC\xCC\xCC\xCC\xCC\xCC";
	unsigned int i;
	printf("%p\n", &shellcode);
	fp = fopen("C:\\Users\\Charles_Truscott\\Desktop\\fin.txt", "w");
	if (fp == NULL) {
		printf("Cannot open file ...");
		return -1;
	}
	for (i = 0; i <= sizeof(buffer) + 512; i += 16) {
		memcpy(&buffer[i], shellcode, 16);
	}
	fwrite(buffer, 1, sizeof(buffer), fp);
	fclose(fp);
	return 0;
}

