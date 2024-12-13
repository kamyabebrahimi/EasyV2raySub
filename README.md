# EasyV2raySub

Easy way to generate your own V2rayN subscription link.

# What's the usage?

Many free v2ray server providers do not provide subscription link, so you have to manually copy the server link when its
updated every time.

Unfortunately, these updates can sometimes be very frequent, that's annoying.

This project can help you generate a
subscription link to get rid of this problem.

# How to use?

## 1 Prepare environment

Requirements:

```
Python >= 3.11
requests >= 2.32.3
beautifulsoup4 >= 4.12.3
```

Other versions should also work.

## 2 Run

# How it works?

The python scripts using a simple regex to match the links which use protocol prefix of `vmess://` and `vless://` in
specific website.

Once getting the links, those links will be writen into `links.txt` file by using the format claimed
in [2dust/v2rayN](https://github.com/2dust/v2rayN/wiki/%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD%E8%AF%B4%E6%98%8E), which
is:
> All links are joined into a string with delimiter `\n`, then encoded into `Base64`.

The hyperlink of the file `links.txt` can be used as a subscription link of V2rayN client.