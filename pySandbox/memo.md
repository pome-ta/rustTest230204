# 📝 2023/02/07

色々と試す用にsandbox を設置

`sandbox` だと、codeSandbox と名前ぶつかりそうだから


`pySandbox` とした

## 2進数

Python の頭の体操として、`lambda` 式とか使って2進数を10進数にしてみた

エラーハンドリングできなくてガバガバだけど、lambda 体験として


`str[::-1` で、取り出す順番を逆順にして、`enumerate` のindex で計算


```
index   7  6  5  4 3 2 1 0
binary  1  0  1  1 1 0 0 1
重み  128 64 32 16 8 4 2 1

```
