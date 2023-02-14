# 📝 2023/02/14

あらためて、数値の型関係を書き直す

私のが、甘々実装で、uint に負の数を入れても、絶対値返してくれているけども

本来は0 を返すでよさそう

# 📝 2023/02/11

## `hash11` の数値的挙動

本の平均値的な内容がどうも理解できていないけども、数値が違うかもしれない。。。

`23011_1915.py` で検証中。

codesandbox のRust で途中まで動かせたっぽいので、値をはりつけ

```
😇 Hello CodeSandbox!
4294967295
1164413355
1
hash 開始
↓ _n
1065353216
↓ _n ^= _n << 1;
1082130432
↓ _n ^= _n >> 1;
1623195648
thread 'main' panicked at 'attempt to multiply with overflow', src/main.rs:22:5
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
[Finished running. Exit status: 101]

```

```main.rs
use glm::floatBitsToUint;

fn main() {
    const UINT_MAX: u32 = 0xffffffffu32;
    let _k: u32 = 0x456789abu32;
    let _p: f32 = 1.0;
    let mut _n = floatBitsToUint(_p);

    println!("😇 Hello CodeSandbox!");
    println!("{}", UINT_MAX);
    println!("{}", _k);
    println!("{:.}", _p);
    println!("hash 開始");
    println!("↓ _n");
    println!("{}", _n);
    _n ^= _n << 1;
    println!("↓ _n ^= _n << 1;");
    println!("{}", _n);
    _n ^= _n >> 1;
    println!("↓ _n ^= _n >> 1;");
    println!("{}", _n);
    _n *= _k;
    println!("↓ _n *= _k;");
    println!("{}", _n);
}


```

最後、掛け算で、なにか怒られているみたい

# 📝 2023/02/09

左シフトの桁溢れってどうするんやろか？

# 📝 2023/02/08

[pome-ta/mathOfRealTimeGraphicsTranscriptionNotes](https://github.com/pome-ta/mathOfRealTimeGraphicsTranscriptionNotes) の疑似乱数確認してるから、行ったり来たりして、点在しちゃうかも

# 📝 2023/02/07

色々と試す用にsandbox を設置

`sandbox` だと、codeSandbox と名前ぶつかりそうだから

`pySandbox` とした

## 2進数

Python の頭の体操として、`lambda` 式とか使って2進数を10進数にしてみた

エラーハンドリングできなくてガバガバだけど、lambda 体験として

`str[::-1]` で、取り出す順番を逆にして、`enumerate` のindex で計算

```
index     7  6  5  4 3 2 1 0
binary    1  0  1  1 1 0 0 1
weight  128 64 32 16 8 4 2 1

```
