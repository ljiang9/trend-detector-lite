# trend-detector-lite

趋势 / 突变检测小工具。移动平均、方向判断、突增突变点检测。零第三方依赖。

## 功能

- 滑窗移动平均；
- 整体方向（up/down/flat）；
- 基于相邻差分中位数的突变点索引。

## 快速开始

```bash
python3 cli.py 1,2,3,4,5,20,6
```

## 无 API Key 如何运行

本工具**完全不需要 API Key**。

## 目录结构

```
trend-detector-lite/
├── trend.py     # 移动平均、方向、突变检测
├── cli.py
├── tests/test_trend.py
├── README.md / LICENSE / .gitignore
```

## 测试

```bash
python3 -m unittest discover -s tests
```

## 许可证

[MIT](./LICENSE)
