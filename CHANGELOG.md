# CHANGELOG

## [0.5.0] - 待定
### Added / 新增
- Domestic region for the United States, Canada, Australia, and Russia (added domestic maps for the above countries)  
  美国、加拿大、澳大利亚和俄罗斯的国内地区判断（新增上述国家国内地图）
### Bug Fixes / Bug 修复：
- Fixed excluded country list display issue  
  修正排除国家列表显示问题

## [0.4.0] - 2025-04-03
### Backend Refactor / 后端数据结构重构：
- Separated question bank into multiple CSV files  
  将街景题库从 questions.json 拆分为多个 csv 文件管理
- Replaced JSON structure with Pandas DataFrame  
  使用 Pandas DataFrame 替代原先的 JSON 加载
- Added excluded_country.csv for country exclusion list  
  新增 excluded_country.csv 记录排除国家
### Bug Fixes / Bug 修复：
- Fixed scoring bugs of the southern hemisphere  
  修正南半球评分问题  

## [0.3.0] - 2025-03-31
### Added / 新增
- Added left-right layout: street clues on the left, map stays visible on the right  
  新增左右布局界面：街景线索显示在左侧，地图展示在右侧，提高操作便利性

### Improvements / 优化
- Improved UI for better browsing and clue coordination  
  UI 更加整洁，便于浏览和交叉参考各类信息

## [0.2.0] - 2025-03-30
### Added / 新增
- Expandable section explaining sun position inference logic (@FionaHU1226)  
  新增下拉区域，提供太阳方位判断说明 (@FionaHU1226)

## [0.1.0] - 2025-03-27
### Added / 新增
- Initial release of the Tuxun helper tool  
  初版 Tuxun 辅助工具上线

- Inference based on license plate color/shape, driving side, sun position, and language  
  支持车牌颜色、形状、行车方向、太阳方位和语言判断

- Automatic country scoring, exclusion, and choropleth map highlighting  
  自动打分 + 自动排除 + 地图国家高亮显示
