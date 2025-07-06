l---
slug: download
title: Скачать
lang: ru
[url_lysator]: http://www.lysator.liu.se/index_en.html
[url_mirror_lysator]: http://ftp.lysator.liu.se/pub/freenet/
[url_mirror_lysator_tor]: http://lysator7eknrfl47rlyxvgeamrv7ucefgrrlhk7rouv3sna25asetwid.onion/pub/freenet/
[url_win_installer]: https://github.com/hyphanet/fred/releases/download/build01503/FreenetInstaller-1503.exe
[url_win_installer_sig]: https://github.com/hyphanet/fred/releases/download/build01503/FreenetInstaller-1503.exe.sig
[url_mac_installer]: https://github.com/hyphanet/mactray/releases/download/v2.1.0/FreenetTray_2.1.0.zip
[url_mac_installer_sig]: https://github.com/hyphanet/mactray/releases/download/v2.1.0/FreenetTray_2.1.0.zip.sig
[url_nix_installer]: https://github.com/hyphanet/fred/releases/download/build01503/new_installer_offline_1503.jar
[url_nix_installer_sig]: https://github.com/hyphanet/fred/releases/download/build01503/new_installer_offline_1503.jar.sig
[url_jnlp_installer]: {static}/assets/jnlp/freenet.jnlp?1503
[url_keyring]: #keyring

Чтобы получить доступ к Hyphanet, сначала необходимо установить основное приложение. 
Hyphanet будет работать в фоновом режиме, и вы сможете использовать свой браузер
для изменения настроек и доступа к контенту.
Есть другие приложения, которые вы можете установить позже, чтобы добавить больше функционала.

<!--
Steps:

* [Download and install Hyphanet][autostart]
* [Add friends (or connect to strangers)][add_friends]
* [Start using Hyphanet!][usage]

[autostart]: #autostart
[add_friends]: #note
[usage]: #usage
-->

Скачайте и установите Hyphanet:

* [Для Windows](#windows)
* [Для Mac OSX](#os-x)
* [Для GNU/Linux & POSIX](#gnulinux-posix)

*Hyphanet - это бесплатное программное обеспечение с открытым исходным кодом, доступное под GPLv2+.
Исходный код находится на [GitHub](https://github.com/hyphanet/fred).*

## Windows

Скачайте и запустите [установщик][url_win_installer]
([gpg подпись][url_win_installer_sig]; [keyring][url_keyring])

[Скачать Hyphanet для Windows][url_win_installer]{: .download-button}

Установка Hyphanet и других необходимых компонентов произойдет автоматически. 
Когда будет готово, в браузере по умолчанию автоматически откроется окно веб-интерфейса Hyphanet.

![]({static}/assets/img/install/1-langselect-windows.png)

Чтобы использовать Hyphanet необходима версия Windows 8.1 или более новая.

Free code signing provided by
[SignPath.io](https://about.signpath.io/), certificate by SignPath
Foundation.

## OS X

Скачайте и запустите [установщик][url_mac_installer]
([gpg подпись][url_mac_installer_sig]; [keyring][url_keyring]).

[Скачать Hyphanet для OS X][url_mac_installer]{: .download-button}

Установка Hyphanet и других необходимых компонентов произойдет автоматически. 
Когда будет готово, в браузере по умолчанию автоматически откроется окно веб-интерфейса Hyphanet.

![]({static}/assets/img/mactray/osx_installer_step2_transparent.png)

Для использования Hyphanet необходима OSX 10.8 или более новая версия.

## GNU/Linux & POSIX

Попробуйте [установщик Java Web Start][url_jnlp_installer].

[Скачать Hyphanet для GNU/Linux & POSIX][url_jnlp_installer]{: .download-button}

Теперь следуйте указаниям установщика:

![]({static}/assets/img/install/1-langselect.png)

Если так не работает:

Вам необходима последняя **Java Runtime Environment** (JRE).
Мы достигли лучших результатов с Oracle Runtime Environment,
которую можно получить через ваш [диспетчер пакетов](
https://en.wikipedia.org/wiki/Package_manager) или на сайте [
http://www.java.com/](http://www.java.com/).

Необходима Java минимум 7 версии, но настоятельно рекомендуется версия 8 или еще более новая.
Следует обновлять Java, чтобы избегать проблемы и повышать производительность.

Откройте терминал и запустите:

    wget 'https://github.com/hyphanet/fred/releases/download/build01503/new_installer_offline_1503.jar' -O new_installer_offline.jar;
    java -jar new_installer_offline.jar;

Для установки в хедлесс системе или в случае возникновения проблем с fontconfig
используйте параметр `-console` и следуйте инструкциям:

    java -jar new_installer_offline.jar -console;

Альтернативно, загрузите [установщик][url_nix_installer]
([gpg подпись][url_nix_installer_sig]; [keyring][url_keyring])
и далее кликнув на файл может сработать на некоторых системах,
но если возникают проблемы, мы рекомендуем использовать командные строки приводимые выше.
Если wget не установлен, его можно установить с помощью диспетчера пакетов:
`sudo apt-get install wget` на Debian или Ubuntu.

**Примечание**: многие дистрибутивы GNU/Linux больше не поставляются с включенным Java Web Start. 
Мы хотели бы сделать пакеты дистрибутивов для более легкой установки.
У нас есть в разработке (дальнейшая работа не идет) [пакет Debian](https://github.com/hyphanet/fred/pull/774),
но мы не получили его стабильную или официальную версию для других дистрибутивов.
Если вы разработчик и хотели бы присоединиться к нам и помочь, мы будем очень признательны!

## Зеркало релизов

Если вы не можете получить доступ к нашим официальным релизам, вы можете попробовать
[http зеркало][url_mirror_lysator] или [tor зеркало][url_mirror_lysator_tor],
предоставленное [Lysator][url_lysator].

## Зеркальная установка

Если у вас есть рабочая папка установки Hyphanet, которую вы скопировали с одной машины Unix
на другую (например, через rsync или unison), включить зеркальную установку не сложно.
Ничего в установке Hyphanet не зависит от IP-адреса хоста; это невозможно, иначе Hyphanet
не сможет работать на машинах, которые получают IP-адреса из пула DHCP.

Все, что на самом деле нужно - это указать системе, на которую вы скопировали файлы,
запускать прокси демон Hyphanet при загрузке. 
Выполните `crontab -l` на исходном компьютере, найдите строку с тегом "FREENET AUTOSTART"
и добавьте ее в свой crontab на зеркальном компьютере.

Однако каждая установка имеет уникальный идентификационный ключ, сгенерированный во время установки.
Если вы попытаетесь запустить два экземпляра с одинаковыми идентификационными данными одновременно,
оба прокси-демона будут сбиты с толку их работа будет нарушена. Не делайте этого!

## Использование Hyphanet

Пожалуйста, попробуйте [пошаговое руководство][url_freesocial] по настройке Hyphanet
и различных его приложений, особенно если установка на OS X.
Мы не несем ответственности за неофициальные сторонние приложения, которые оно рекомендует (включая FMS),
но многие пользователи и разработчики Hyphanet используют их.

### Фаерволы и роутеры

Hyphanet должен нормально работать с большинством маршрутизаторов, но если у вас возникли проблемы
и у вас есть брандмауэр или маршрутизатор, нажмите [**сюда**](help.html#firewall) для
получения дополнительной информации.

### Итак, он работает, что мне делать?

Когда установщик закрывается, он должен открыть окно браузера с мастером установки. 
Здесь вы можете настроить основные параметры, а затем начать использовать Hyphanet.
Вы можете получить доступ к Hyphanet позже через меню в системном трее (в нижнем правом углу экрана).
Или используйте ярлык 'Browse Hyphanet' на рабочем столе и/или в меню 'Пуск'. Если это не работает,
вставьте этот URL [http://127.0.0.1:8888/](http://127.0.0.1:8888/) в своем веб-браузере.

Для лучшей безопасности стоит использовать отдельный браузер для Hyphanet, предпочтительно
в режиме конфиденциальности. В Windows, меню в системном трее будет пытаться использовать
Chrome в режиме инкогнито, если это возможно. Internet Explorer плохо работает с Hyphanet,
Firefox и Opera широко используются.

Если вы знаете кого-то, кто также использует Hyphanet, вы можете улучшить свою безопасность
и помочь построить надежную сеть, подключившись к его ноде. Сначала откройте страницу
[Добавить друга](http://127.0.0.1:8888/addfriend/). Вы и ваш друг должны скачать свою
'ссылку на ноду' (node reference). Отправьте этот файл вашему другу и добавьте ссылку на его ноду,
используя форму внизу страницы. Когда ссылки будут добавлены с двух сторон, нода вашего друга
должна появиться на странице 'Друзья', вероятно, как 'CONNECTED' или 'BUSY'. Вы можете установить
имя для своего узла на странице конфигурации, чтобы было легче увидеть, кто это.
Добавляйте только те ноды, которые принадлежат людям, которых **вы действительно знаете**,
будь то онлайн или офлайн, так как добавление незнакомых людей вредит производительности и
не сильно повышает безопасность (это могут быть плохие ребята!).

### Итак, я присоединен, что мне делать?

Hyphanet включает в себя анонимные веб-сайты (они же 'фрисайты'), общий доступ к файлам,
поиск и многое другое, но вы также можете использовать сторонние приложения для чатов,
обмена файлами, помощи в загрузке бесплатных сайтов и так далее.

В [Руководство по социальным сетям Hyphanet](http://freesocial.draketo.de/) есть объяснение,
как настроить основные сторонние инструменты, включая электронную почту, форумы
и микроблоггинг (Sone, немного похож на Twitter).

### Это не работает, что теперь?

Если у вас возникли проблемы с установкой или запуском Hyphanet, см. [Базу знаний][kb_url],
[FAQ][faq_url], [чат][chat_url] или [списки рассылок][ml_url].

[kb_url]: https://support.freenetproject.org/kb
[faq_url]: help.html#faq
[chat_url]: help.html#irc
[ml_url]: help.html#mailing-lists

### Требования к оборудованию

Как правило, процессора 1 ГГц и 1 ГБ оперативной памяти достаточно. Hyphanet будет работать и
на меньших системах, но использует не менее 128 МБ оперативной памяти. Поэтому, если система
не делает ничего другого, она будет с трудом работать имея менее чем 512 МБ. Тем не менее,
процессор представляет собой меньшую из проблем; люди, как известно, запускали его на 400 МГц
процессорах Pentium 2 или ATOM, хотя загрузка и просмотр информации в сети будут медленными.

Hyphanet будет использовать часть вашего диска для хранения данных, вы можете выделить любой размер
от 100 МБ и более. Но мы рекомендуем выделить минимум 1 ГБ. Hyphanet также использует дисковое
пространство для ваших загрузок из сети. Использование памяти Hyphanet составляет примерно 256 МБ
плюс 400 КБ на каждые 2 ГБ хранилища данных.

На 64-битном Windows мы установим 32-битную виртуальную машину Java из-за ограничений
[Java Service Wrapper](http://wrapper.tanukisoftware.org/doc/english/download.jsp).

### Обновление

Hyphanet предоставляет механизм обновления-через-Hyphanet: он будет автоматически обновляться с
других нод Hyphanet и это обычно будет работать, даже если не будет нормально работать роутинг
из-за того, что они слишком новые. Это анонимно и безопасно, и мы рекомендуем людям использовать это.
Однако, если что-то серьезно сломано, вы можете обновить свою ноду вручную с наших серверов:

* Пользователи Windows могут обновиться до последней стабильной версии Hyphanet,
  запустив "update.cmd" в папке Hyphanet.
* Пользователи OS X, GNU/Linux или POSIX могут выполнить обновление,
  запустив скрипт update.sh в папке Hyphanet.

[url_freesocial]: http://freesocial.draketo.de/

## Добавить друзей (или подключиться к незнакомцам)

Если вы знаете других людей, которые также используют Hyphanet,
вы можете [добавить их в Друзья][url_addfriend].
Это сделает вас более защищенными от атак на инфраструктуру проекта Hyphanet
([сидноды][url_seednode_info]).

Как только вы подключитесь к 5 или более друзьям, вы можете включить **режим высокой безопасности**.
В нем Hyphanet будет подключать вас только к вашим друзьям. 
Это делает ваше использование Hyphanet практически не поддающимся к обнаружению,
но вы все еще можете получить доступ к остальной части сети через друзей друзей друзей ....

Вы не должны добавлять друзей прямо сейчас. 
Если вы используете 'низкий' или 'нормальный' уровень безопасности,
Hyphanet автоматически подключится к незнакомым людям и будет нормально работать.
Тем не менее, ваше (или какое-то другое) правительство может выяснить, кто вы,
приложив какое-то количество усилий. Будьте осторожны!

[url_addfriend]: http://127.0.0.1:8888/addfriend/
[url_seednode_info]: https://wiki.freenetproject.org/Seed_nodes#Seed_node

## Проверка подписей

Загрузите [ключи подписи Проекта Hyphanet][url_keyring] и импортируйте их в свою связку ключей:

        pub   2048R/0xEAC5EBF07AA9C2A3 2013-04-29
              Key fingerprint = DBB7 7338 3BC3 49C9 5203  ED91 EAC5 EBF0 7AA9 C2A3

        pub   4096R/0x00100D897EDBA5E0 2013-09-21 [expired: 2016-09-08]
              Key fingerprint = 0046 195B 2DCA B176 D394  09CD 0010 0D89 7EDB A5E0
        uid                  Steve Dougherty (operhiem1 Release Signing Key) <steve@asksteved.com>
        sub   4096R/0x7BF0F7B36AC8B380 2013-09-21 [expired: 2016-09-15]

        pub   4096R/0xFF24CA421946AA94 2013-09-24 [expires: 2018-09-23]
              Key fingerprint = B76D 4AA7 96D8 403E ED78  C9F9 FF24 CA42 1946 AA94
        uid                  Matthew Toseland (2013-2018 key, higher key length) <matthew@toselandcs.co.uk>
        uid                  Matthew Toseland (2013-2018 key, higher key length) <toad@amphibian.dyndns.org>
        sub   4096R/0xF877E62895C42009 2013-09-24 [expires: 2018-09-23]

        pub   4096R/0xB67C19E817A8D846 2016-01-02 [expires: 2018-01-03]
              Key fingerprint = 5D77 D9A4 2E28 0F5A FF8F  2EBF B67C 19E8 17A8 D846
        uid                  Stephen Oliver <steve@infincia.com>
        sub   4096R/0x9BCDD1614041F59E 2016-01-02 [expires: 2018-01-03]
        sub   4096R/0x1652EBA5AC1BB386 2016-01-02 [expires: 2018-01-03]
        sub   4096R/0x38A62E479684F2F2 2016-01-02 [expires: 2018-01-03]

        pub   4096R/0xB41A6047FD6C57F9 2017-02-23
              Key fingerprint = B30C 3D91 069F 81EC FEFE  D0B1 B41A 6047 FD6C 57F9
        uid                  Arne Babenhauserheide (freenet releases) <arne_bab@web.de>
        uid                  Arne Babenhauserheide (ArneBab) <arne_bab@web.de>

[url_keyring]: {static}/assets/keyring.gpg
