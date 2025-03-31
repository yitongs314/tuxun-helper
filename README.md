# 🌍 Tuxun Helper | 图寻辅助工具

This is a street-view reasoning assistant App designed for Tuxun (GeoGuessr) players.  
一个专为图寻玩家设计的街景推理辅助App。

You can input details you observe in a street view (such as language, license plates, buildings, utility poles, etc.),  
你可以输入你在街景中看到的细节（语言、车牌、建筑、电线杆等），

The App automatically highlights likely countries and eliminates impossible ones, helping you narrow down your guess!  
系统将自动高亮可能国家，并排除不符合条件的地区，帮助你快速锁定答案！

---

## Live Demo | 在线体验地址

👉 [Click here to try it online](https://tuxun-tool.streamlit.app/)  
👉 [点击这里立即体验](https://tuxun-tool.streamlit.app/)

---

## 支持的线索类型 | Supported Clues

- **Language** (with image/text hints + country exclusion)  
  **语言**（图文辅助 + 国家排除） 

- **License plate colors and shapes**  
  **车牌颜色与形状**  

- **Driving side** (automatically excludes incompatible countries)  
  **行车方向**（左/右行车自动排除国家）  

- **Sun position** (for determining south / north hemisphere)  
  **太阳方位**（判断南/北半球）  

- **Utility poles, architectural style, vegetation** (coming soon)  
  **电线杆、建筑风格、植被**（持续扩展中）  

---

## Usage | 使用说明

This project is built with [Streamlit](https://streamlit.io/) and deployed on Streamlit Cloud.  
本项目基于 [Streamlit](https://streamlit.io/) 构建，部署于 Streamlit Cloud 平台。

To run locally:  
如需本地运行：

```bash
git clone https://github.com/yitongs314/tuxun-helper.git
cd tuxun-helper
pip install -r requirements.txt
streamlit run tuxun_helper.py
```

---

## Changelog | 更新日志

📄 [View full changelog](CHANGELOG.md)  
📄 [查看开发日志](CHANGELOG.md)
