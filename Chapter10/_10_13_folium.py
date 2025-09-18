import folium

## 지도 생성 (서울 시청 (37.5665, 126.9780) 중심, 확대 레벨 12)
map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

## 마커 추가
# 한국방송통신대학교 대학본부 (37.5792, 127.0029)
folium.Marker([37.5792, 127.0029],popup='방통대').add_to(map)

## 지도를 HTML 파일로 저장
map.save("map_visualization.html")