---
title: "Weekend of Code" hackathon results
date: 2015-12-20
layout: content
---

During the hackathon we got some changes done:

- [Fix uploads stalling when using MAXIMUM physical security.][1]
- [Fix lots of "setNativePriority(X) has failed!"][2]
- [Fix Bokmål localization loading.][3]
- [Fix JVM version string parsing.][4]
- [Fix and add test for broken localization substitution token pairs.][5]
- [Remove Gantros Index][6] because it stopped updating.
- [Remove Linkageddon][6] because it stopped updating.
- [Remove deprecated negtype crypto.][7]
- [Order alerts by date.][8]
- [Progress toward Freemail "to" field autocomplete.][9]
- Progress toward changing the language setting in Winterface.
- Progress toward building and verifying dependencies for [Fred][10] and [Winterface][11] using [Gradle][12] and [gradle-witness][13].

If we're able to get final changes ready build 1471-pre3 will be released the weekend of January 2nd.

[1]: https://github.com/freenet/fred/pull/438
[2]: https://github.com/freenet/fred/pull/435
[3]: https://github.com/freenet/fred/pull/426
[4]: https://github.com/freenet/fred/pull/437
[5]: https://github.com/freenet/fred/pull/421
[6]: https://github.com/freenet/fred/pull/433
[7]: https://github.com/freenet/fred/pull/439
[8]: https://github.com/freenet/fred/pull/418
[9]: https://github.com/Dr-Tensor/plugin-Freemail/tree/master
[10]: https://github.com/freenet/fred/tree/gradle
[11]: https://github.com/ademan/winterface/tree/gradle-witness-1
[12]: https://gradle.org/
[13]: https://github.com/WhisperSystems/gradle-witness
