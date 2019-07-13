#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int main() {
  char mesaj[50];
  int anahtar,i;
  scanf("%s",&mesaj);
  strupr(mesaj);
  scanf("%u",&anahtar );
  for (i = 0; i < strlen(mesaj); i++) {
    mesaj [i]=  (char)(((int)mesaj[i]-65+anahtar)%26+65);
  }
  printf("%s",mesaj );

  return 0;
}
