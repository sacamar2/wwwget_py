# wwwget_py
It is a Windows WSL wget python lib to use it for HTML folder directories in paralel

## What can you do with this Lib?
Currently, this library only allow you to download files from a continuous folder system accessible through a HTTP request.

## Why does this Lib exists?
I came across a bunch of folders on an URL but wget kept creating strange artifacts and unwanted indexes. I tried many configurations, but I could get what I needed.

Probably, wget can do the same this lib does. Because of it, I wanted to go a bit further. This lib does in paralel what wget does linearly, this means faster downloads.

## Advantage/Disadvantage vs wget
## Advantage wwwgetpy vs wget

| Advantage      | Disadvantage |
| ----------- | ----------- |
| Paralel download | Dependency with the OS and WSL |
| __Future retries__ |  |
| Able to implement it into any other Python Script using classes | You can only implement it via "os" package |

## Why does this library needs wget and Windows OS?
This lib can only be executed on Windows using WSL because that was my local configuration. I trust on the capacity of wget and I wanted to have as my base to ensure a solid product.

## Next steps
Recently, I think to move away of wget and decrease the tech dependencies so this resource can be used easily anywhere.

In addition, I want to add retries to avoid robots blocking easily.
