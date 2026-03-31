The `Tier` of a module does not reflect its `difficulty`.

**Note:** If you have an annual subscription, then included modules will cost you 0 cubes, while still giving you back their reward.
will also unlock walkthroughs for all exercises
## What are Paths > Modules > Sections ?

Largest : path
then sub division : module
then sub division : section

A `section` is the smallest building block in the HTB Academy structure. Each section covers a specific area in the larger module topic, and is `designed to be completed in one sitting`.

For example, in this `Intro to Academy` module, this `Sections` section discusses sections!

**Tip:** You can estimate how long a path will take to complete by checking the duration mentioned underneath the path's title. This represents the sum of the `estimated time for completion` of each module in the path "in 8-hour work days".
## Types of Sections

There are two types of sections: `Theory Sections` and `Interactive Sections`.

`Theory sections` do not contain any practical elements. Instead, they build the foundational knowledge that is necessary to understand any upcoming practical/interactive lessons, and establish the basics for the entire module.

On the other hand, `interactive sections`, which are denoted with a small , form the majority of sections within HTB Academy. This is where you will learn through practical examples and demos.

![Checklist with items: Introduction, Sections, and Exercises, each marked complete.](https://academy.hackthebox.com/storage/modules/15/table_of_content.png)

You are always `highly encouraged to re-apply what you learned` throughout any interactive section, to ensure you get to practice what you learned.

## What is an Exercise?

An exercise will usually have an accompanying `Docker target` or `VM target(s)`. A target can be started by clicking on `Click here to spawn the target system!`, which will be populated with its access details, in the format `http://<ip>:<port>`. It may also provide authentication details, in the form of a `username` and `password`.

## Docker Targets

**Note:** You can spot a docker target by its lack of a VPN button, as no VPN connection is required to access it.

## Openvpn
Save the file on your VM of choice and connect to it using the following command:

`sudo openvpn academy-regular.ovpn`

If you have already running VPN files, use `sudo killall openvpn` to kill them.

[![](https://downloads.intercomcdn.com/i/o/1044982399/ac79de14b241aa38c38f8b0b/ScreenRecording2024-05-08at12_59_54PM-ezgif_com-video-to-gif-converter.gif?expires=1754991900&signature=c9cef33074e4653f60c0ac9c511658b06036bab5ec293f766cfcf684e17dec40&req=dSAjEsB2n4JWUPMW1HO4zQPJF5OKASJdzSi87KFnN2l06WuRsdErPNuVMggq%0AhZ5nhc%2BwWDYnaeNNkm8%3D%0A)](https://downloads.intercomcdn.com/i/o/1044982399/ac79de14b241aa38c38f8b0b/ScreenRecording2024-05-08at12_59_54PM-ezgif_com-video-to-gif-converter.gif?expires=1754991900&signature=c9cef33074e4653f60c0ac9c511658b06036bab5ec293f766cfcf684e17dec40&req=dSAjEsB2n4JWUPMW1HO4zQPJF5OKASJdzSi87KFnN2l06WuRsdErPNuVMggq%0AhZ5nhc%2BwWDYnaeNNkm8%3D%0A)

Once you see `Initialization Sequence Completed` you are ready to go, **do not close the terminal tab** as this will kill your connection, open a new tab and start working from it.

[![](https://downloads.intercomcdn.com/i/o/1044983046/5841a76f951c9e1ce745d821/image.png?expires=1754991900&signature=d9f164396936f87299abf6b16db4094b9cfa8560988b3c475531ecf93e3ac334&req=dSAjEsB2noFbX%2FMW1HO4zQxat%2BhKUtvkbo3tx1B2O%2BMAbNRZ6ILlu4Q1yxot%0A%2B2fO42iC6KAWMeh7Urs%3D%0A)](https://downloads.intercomcdn.com/i/o/1044983046/5841a76f951c9e1ce745d821/image.png?expires=1754991900&signature=d9f164396936f87299abf6b16db4094b9cfa8560988b3c475531ecf93e3ac334&req=dSAjEsB2noFbX%2FMW1HO4zQxat%2BhKUtvkbo3tx1B2O%2BMAbNRZ6ILlu4Q1yxot%0A%2B2fO42iC6KAWMeh7Urs%3D%0A)

