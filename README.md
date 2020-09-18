# Voice Channel Fetcher

> Python script for fetching the user's selected voice channel

Fetching a voice channel is already possible by enabling the Discord's "Developer Mode" and copying the channel ID.
Unfortunately that's not the case with Direct Message conferences, which is currently really hard to find this info.

Why needing that at all cost? Currently, the [Discord StreamKit](https://streamkit.discord.com/overlay) only supports servers, but not Direct Message conferences, and maybe some people would like to use this widget without having to join a server's voice channel. This tool can display the voice channel the user is currently connected no matter the place, in our case knowing this hidden ID.

When running the program, it'll display what we need before going to the second phase: updating the widget's URL.

```
Selected Voice Channel: "A Voice Channel" (ID: 645988483891337384)
```

The process is fairly easy, all you need is to generate a widget URL of your choice then updating like the following example:

```
                                                               The part to update
                                                               v----------------v
https://streamkit.discord.com/overlay/voice/375847144521812032/382621880409343528
```

Then replace this part by the ID returned by the program:

```
https://streamkit.discord.com/overlay/voice/375847144521812032/645988483891337384
```

Now the widget should display the voice channel you wanted, even Direct Message conferences.
