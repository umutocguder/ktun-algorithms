DFS(G, s){
  for each u in V { // İlk değerleri atama
      color[u] = white;
      pred[u] = NULL;
  } //end-for
time = 0;
for each u in V
if (color[u] == white) // Ziyaret edilmemiş düğüm bulundu
      DFSVisit(u); // Yeni bir aramaya başla
} // end-DFS

DFSVisit(u){ // u üzerinde yeni bir arama başlat
  color[u] = gray; // u’yuziyaret edildi şeklinde işaretle
  d[u] = ++time;
    for each v in Adj[u] {
      if (color[v] == white){ // Eğer komşu v bulunmadı ise
      pred[v] = u; // … önceki olarak kaydet
      DFSVisit(v); // …v’yiziyaret et
      } //end-if
    } //end-for
  color[u] = black; //u ile işimiz bitti.
  f[u] = ++time;
  } //end-while
} //end-DFSVisit
