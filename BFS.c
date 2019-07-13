BFS(G, s){
for each u in D-{s} { // İlk değerleri atama
color[u] = white;
d[u] = SONSUZ;
pred[u] = NULL;
} //end-for
color[s] = GRAY; // s’nin ilk değerlerini atama
d[s] = 0;
pred[s] = NULL;
K= {s}; // s’yi kuyruğa koy
while (K boş değilken){
u = Cikart(K); // u bir sonraki düğüm
for each v in Adj[u] {
if (color[v] == white){ // Eğer v bulunmadı ise
color[v] = gray; // … Bulundu şeklinde işaretle
d[v] = d[u] + 1; // … uzaklığı ayarla
pred[v] = u; // … öncekini ayarla
Ekle(v); //… kuyruğa ekle
} //end-if
} //end-for
color[u] = black; // u ile işimiz bitti
} //end-while
} //end-BFS
