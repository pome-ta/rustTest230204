
# 📝 2023/02/11

## cargo でCrate をいれてみる

`floatBitsToUint` というそのものが

[glm::builtin::floatBitsToUint - Rust](https://dche.github.io/glm-rs/glm/builtin/fn.floatBitsToUint.html)

という`glm` にあるらしい。。。

Crate という、パッケージ的なものらしいので、codesandbox に入れてみる

## `Cargo.toml`

直書きを試してみたが、

```Cargo.toml
[package]
name = "workspace"
version = "0.1.0"
edition = "2021"

[dependencies]
glm = "0.2.3"

```

blocking が何か？で、引き連れて入るはずの、`num` というCrate が入らなかった

## CodeSandbox のterminal より

`cargo add glm` というコマンドがあったので、terminal　から入れたら無事に入ったっぽい

# 📝 2023/02/07

Rust の文法とか基本的なところから、ダラダラと書くところ

拡張子は、Pythonista3 でも開きやすいように`.py` か、`.js`
