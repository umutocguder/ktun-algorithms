//MATRİS GÖSTERİMİ
int Matris [MAX_DUGUM,MAX_DUGUM];
KOMŞULUK LİSTESİ (ADJACENCY LIST)
typedef struct dugum
{int dugum_no;
struct dugum *pNext;
}DUGUMLER;
typedef struct liste
{
DUGUMLER satir[MAX_DUGUM];
}LISTELER;
