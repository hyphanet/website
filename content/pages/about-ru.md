---
title: About
lang: ru
---

## Что такое Freenet?

> Я постоянно переживаю за своего ребенка и за Интернет, хотя она еще слишком мала,
> чтобы войти в систему. Вот, о чем я беспокоюсь. Я переживаю, что через 10 или 15 лет
> она придет ко мне и скажет: 'Папа, где ты был, когда они забрали свободу прессы из Интернета?'

--Майк Годвин, [Фонд электронных рубежей](https://www.eff.org/)

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zu9gM3_gIfM"
	frameborder="0" allowfullscreen></iframe>
</div>

Freenet - это бесплатное программное обеспечение, которое позволяет анонимно
обмениваться файлами, просматривать и публиковать "фрисайты" (веб-сайты, доступные
только через Freenet) и общаться на форумах, не опасаясь цензуры. Freenet
децентрализован для того, чтобы сделать его менее уязвимым к атакам. При использовании
Freenet в режиме "darknet", когда пользователи подключаются только к своим друзьям,
их очень трудно обнаружить.

Общение между нодами (узлами) Freenet зашифровано и маршрутизируется через другие
ноды, чтобы было крайне сложно установить кто запрашивает информацию и какой у нее контент.

Пользователи вносят свой вклад в сеть, предоставляя часть пропускной способности
своего интернет-соединения и часть своего жесткого диска (так называемое "хранилище данных")
для хранения файлов. Файлы автоматически сохраняются в сети или удаляются из нее в зависимости
от их популярности: наименее популярные выбрасываются, чтобы освободить место для нового или
более популярного контента. Файлы зашифрованы, поэтому пользователь, как правило, не знает что
именно находится в хранилище данных на его компьютере, и, мы надеемся, не несет ответственность
за эти данные. Чат-форумы, веб-сайты и функции поиска - все построены на основе этого
распределенного хранилища данных.

С момента начала проекта, Freenet был скачан более 2 миллионов раз и использовался
для распространения цензурированной информации по всему миру, включая такие страны, как
Китай и страны Ближнего Востока. Идеи и концепции, которые впервые появились именно во
Freenet, оказали значительное влияние на академический мир. Наша статья 2000 года
"Freenet: распределенная система анонимного хранения и поиска информации" ("Freenet:
A Distributed Anonymous Information Storage and Retrieval System") была самой цитируемой
статьей по информатике 2000 года по версии Citeseer. Также, Freenet вдохновил написание
серии статей в области права и философии. Ян Кларк, создатель и координатор проекта Freenet,
был включен в список 100 лучших новаторов 2003 года журналом MIT's Technology Review.

Одной из важных разработок последних лет является режим "darknet" -
функционал, которым могут похвастаться очень немногие сети. Подключаясь только к тем людям,
кому доверяют, пользователи могут значительно снизить свою уязвимость, в то же время,
сохраняя возможность подключаться к глобальной сети через своих друзей, друзей своих друзей
и так далее. Это позволяет людям использовать Freenet даже в тех местах, где он может быть
незаконным: поскольку Freenet не полагается на прокладывание туннеля в "свободный мир",
правительствам очень сложно заблокировать его.

*Ян Кларк пишет*

1.  [Дисклеймер](#a-disclaimer)
2.  [Рекомендованное предварительное чтение](#suggested-prior-reading)
3.  [Важность свободного обмена информацией](#the-importance-of-the-free-flow-of-information)
4.  [Цензура и свобода](#censorship-and-freedom)
5.  [Решение](#the-solution)
6.  [Иногда цензура нужна, разве нет?](#isnt-censorship-sometimes-necessary)
7.  [Но зачем нужна анонимность?](#but-why-is-anonymity-necessary)
8.  [Что такое Копирайт?](#and-what-of-copyright)
9.  [Но как люди творчества будут вознаграждены за свою работу без Копирайта?](#but-how-will-artists-be-rewarded-for-their-work-without-copyright)
10.  [Альтернативы копирайту](#alternatives-to-copyright)

## Философия Freenet

1. ### Дисклеймер {#a-disclaimer}

    Есть много причин, почему люди участвуют в разработке Freenet. Некоторые
    разделяют взгляды, изложенные в этом документе; некоторые разделяют вариации этих
    взглядов, и также заинтересованы в успехе проекта; а некоторым просто нравится решать
    сложные и интересные технические задачи проекта. Ниже изложены мысли, которые в
    первую очередь побудили меня создать такую систему, но они не обязательно отражают
    взгляды всех участников проекта Freenet.

2. ### Рекомендованное предварительное чтение {#suggested-prior-reading}

    Для того, чтобы этот документ имел смысл, вам, вероятно, стоит понимать, что такое Freenet.
    [Здесь](about.html#introduction) вы можете получить общее представление о проекте.

3. ### Важность свободного обмена информацией {#the-importance-of-the-free-flow-of-information}

    Свобода слова в большинстве западных культур, как правило, считается одним из
    самых важных прав, которые может иметь каждый человек. Почему свобода обмена идеями и
    мнениями так важна? Есть несколько способов ответить на этот вопрос.

    1. ### Общение - это то, что делает нас людьми

        Наша способность передавать сложные и абстрактные понятия - одна из наиболее
        очевидных различий между человечеством и животным миром. Несмотря на то, что мы
        постоянно обнаруживаем, что коммуникационные способности животных являются более
        сложными, чем предполагалось ранее, маловероятно, что любое другое животное приблизится
        к нашему собственному уровню способностей в этой области.

    2. ### Знания - это хорошо

        Большинство людей, у которых есть выбор: знать что-то или нет, предпочитает
        получать больше информации. Войны были выиграны и проиграны из-за того, кто был более
        проинформирован. Информация позволяет нам принимать более правильные решения, и в
        целом улучшать нашу способность выживать и быть успешными.

    3. ### Демократия предполагает высокий уровень проинформированности населения

        В современном мире многие живут в странах с демократическим правительством,
        а те, кто нет, вероятно, хотят этого. Демократия - это ответ на вопрос о том, как
        создавать лидеров, не давая им возможности злоупотреблять властью. Это достигается
        путем предоставления населению полномочий регулировать свое правительство с помощью
        голосования, однако право голосовать не обязательно означает, что вы живете в
        демократической стране. Чтобы население эффективно регулировало свое правительство,
        необходима информация о его работе. Это система обратной связи, которая может быть
        нарушена, если правительство получит право контролировать доступную для населения информацию.

4. ### Цензура и свобода {#censorship-and-freedom}

    Каждый человек ценит свою свободу. И, на самом деле, многие считают ее
    настолько важной, что готовы за нее умереть. Людям нравится думать, что они
    могут свободно формировать и придерживаться любых мнений, которые им нравятся,
    особенно это проявляется в западных странах. Теперь представьте, что кто-то была
    бы возможность контролировать доступную для вас информацию. Это дало бы им
    возможность манипулировать вашим мнением, скрывая от вас какие-то факты, преподнося
    вам ложь и подвергая цензуре все, что ей противоречит. Это не какая-то оруэлловская
    выдумка, врать своему населению - это обычная практика большинства западных
    правительств. Люди настолько привыкли к обману со стороны правительства, что считают это
    само собой разумеющимся. Несмотря на то, что это подрывает те самые демократические
    принципы, которые собственно оправдывают существование правительства.

5. ### Решение {#the-solution}

    Единственный способ обеспечить эффективность демократии - это сделать так,
    чтобы правительство не могло контролировать процесс распространения информации,
    общения среди людей. Пока все, что мы видим и слышим, фильтруется, мы не свободны
    по-настоящему. Цель Freenet - позволить людям, которые хотят поделиться
    информацией, сделать это.

6. ### Иногда цензура нужна, разве нет? {#isnt-censorship-sometimes-necessary}

    Конечно, проблема не в том, хорошо это или плохо, и многие думают, что
    цензура - это нужная вещь при определенных обстоятельствах. Например, в некоторых
    европейских странах распространение информации, которая считается расистской,
    является незаконным. Правительства стремятся препятствовать продвижению идей,
    которые считаются вредными для общества. Однако, есть два возражения на этот счет.
    Во-первых, вы не можете позволить людям у власти ввести "хорошую" цензуру, не
    позволяя им также вводить "плохую" цензуру. Для того, чтобы ввести любую форму
    цензуры, правительство должно иметь возможность контролировать и, следовательно,
    ограничивать общение. Уже есть критика, что цензура антирасизма во многих
    европейских странах препятствует законному историческому анализу таких событий,
    как вторая мировая война.

    Вторым доводом является то, что эта "хорошая" цензура не эффективна,
    даже если она не проникает в другие области. Например, как правило, можно намного
    лучше убедить кого-то в чем-то, если показать аргументы против и после возразить им.
    К сожалению, предотвращение осведомленности людей о зачастую изощренных аргументах,
    используемых расистами, делает их уязвимыми к этим аргументам, когда они сталкиваются с ними.

    Конечно, первый аргумент сильнее и остается правдивым, даже если вы
    не согласны со вторым. По сути, у вас либо есть цензура, либо нет.
    Среднего не дано.

7. ### Но зачем нужна анонимность? {#but-why-is-anonymity-necessary}

    Свобода слова не возможности без возможности сохранять анонимность.
    Большая часть цензуры является ретроспективной. Как правило, намного легче
    ограничить свободу слова, если наказывать тех, кто ее уже применил, нежели
    предотвратить ее попытки. Единственный способ избежать это - сохранять
    анонимность. Идея, что вы не можете доверять анонимной информации является
    распространенным заблуждением. Это не обязательно верно, используя цифровые
    подписи, люди могут создать безопасный анонимный псевдоним, которому со временем
    ругие станут доверять. Freenet включает в себя механизм, "subspaces",
    который делает это возможным.

8. ### Что такое Копирайт? {#and-what-of-copyright}

    Конечно, вопрос об авторском праве во Freenet вызвал много внимания
    со стороны общества, в связи с этим я коротко скажу свое мнение на этот счет.
    Основная проблема с авторским правом заключается в том, что для его соблюдения
    необходимо мониторить коммуникации. Таким образом не возможна гарантия свободы
    слова, если кто-то следит за всем, что вы говорите. Это важно, большинство
    людей не видят или не берут во внимание этот момент при обсуждении вопроса об
    авторском праве. Поэтому позвольте мне прояснить:

    > *Вы не можете гарантировать свободу слова и применять закон об авторском праве*

    Именно по этой причине Freenet, система, разработанная для защиты
    Свободы Слова, должна препятствовать контролю соблюдения авторских прав.

9. ### Но как люди творчества будут вознаграждены за свою работу без Копирайта? {#but-how-will-artists-be-rewarded-for-their-work-without-copyright}

    Во-первых, даже если авторское право было единственным способом получить
    вознаграждение за свою работу, я бы сказал, что свобода важнее профессионального
    творчества (те, кто утверждают, что у нас не будет искусства, не понимают творчества:
    люди всегда будут создавать, это компульсивное желание, вопрос только в том,
    смогут ли они этим зарабатывать на жизнь).

    Во-вторых эффективность Копирайта сомнительна даже сейчас. Музыкальная индустрия
    наиболее заметно выступает против улучшений в коммуникационных технологиях,
    тем не менее по мнению многих артистов, которым Копирайт должен приносить доход,
    он не работает. Скорее это позволило посредникам получить контроль над механизмами
    дистрибуции, в ущерб как художникам, так и общественности.

10. ### Альтернативы копирайту {#alternatives-to-copyright}

    К счастью, до этого не дойдет. Есть много альтернативных способов
    вознаграждения артистов. Самым простым является добровольный платеж. Это продолжение
    системы патронажа, которая часто использовалась для вознаграждения художников до
    авторского права, когда богатый человек финансировал артиста, чтобы позволить им
    творить на постоянной основе. Интернет дает возможность продления этой идеи,
    когда вместо одного источника финансовой поддержки, вы могли бы иметь сотни тысяч,
    которые вкладывают небольшие суммы денег через Интернет.

    Собственно говоря мы также практикуем это, 15 марта 2001 года проект Freenet
    начал принимать пожертвования, и в течение недели мы собрали более 1000 долларов.

### Главные участники проекта на сегодняшний день


Ян Кларк

: Проект Freenet основан на работе Яна "Распределенная децентрализованная
система хранения и поиска информации". Ян начал проект Freenet примерно в
июле 1999 года и продолжает его координировать.
Узнайте больше об Яне на его [личном сайте](http://blog.locut.us/).

Мэтью Тоузеленд

: Мэтью работал над Freenet еще до выхода 0.5. Его и работа других
разработчиков привела к значительному улучшению производительности и стабильности сети.

Оскар Сандберг

: Оскар также был одним из первых авторов проекта Freenet, и сделал несколько
важных теоретических прорывов, которые привели к началу Freenet 0.7,
смотрите страницу с документами.

Флорент Даигниере

: С 2003 года Флорент улучшил различные аспекты программного обеспечения и проводил
его системное администрирование. На основной работе он занимает должность технического
директора консалтинговой фирмы по безопасности [Matta Consulting](https://www.trustmatta.com)
и в настоящее время работает над [safepass.me](https://safepass.me) -
фильтром паролей Active Directory.

Майкл Роджерс

: Майкл в основном участвовал в создании подробных симуляций в рамках инициатив
программы компании Google, Google Summer of Code. Он помог в разработке
[нового транспортного уровня](https://old-wiki.freenetproject.org/NewTransportLayer).

Стив Догерти

: Текущий релиз менеджер. Он присоединился к GSoC 2013 и был движущей
силой в решении давних проблем в Freenet.


xor

: Разработчик плагина Web of Trust и Freetalk. Он работал над Web of Trust
в режиме не полного рабочего дня в течение одного года и теперь снова работает волонтером.


Девид (Bombe) Роден

: Разработчик инструмента jSite для создания сайтов и социальной сети Sone во Freenet.


Ксимин Луо

: Разработчик операционной системы Debian, который в настоящее время работает над сборкой Freenet.


Берт Массоп

: Работает над основной частью Freenet и везде, где это необходимо.


TheSeeker

: Является соавтором Freenet на протяжении длительного времени, который, кроме этого,
помогает поддерживать связь между основными разработчиками и пользователями в активных группах.


Tommy[D]

: Упаковщик ОС Gentoo, который распутал все зависимости Freenet и аккуратно упаковал его в Gentoo.


Арне Бабенхаузерхейд

: Занимается поддержкой pyFreenet и infocalypse. Он также пишет статьи и учебные пособия для Freenet.


#### Переводчики

Благодаря кропотливой работе команды людей с разным опытом и профессиями у Freenet и этого
веб-сайта есть переводы на многие языки.


#### Многие выдающиеся хакеры

В этом списке отсутствуют многие авторы фрисайтов, разработчики плагинов и множество других
людей, которые внесли свой вклад различными способами.


### Anonymous Contributors


Eleriseth

: Works on Freenet core and communicates via FMS.


Somedude

: The developer of the Freenet-based Forum system FMS, of FreenetHG and
of FLIP, chat over Freenet.


The folks from Frost

: A group of users and programmers who use an old spammable
Freenet-based forum system which has been abandoned by most of the
core developers. They are active, however, and though it takes time
for their contributions to reach to core development, they take part
in Freenet development.



### Previous Contributors

Thomas Markus

: A dutch developer and statistic-enthusiast. He now works at Topicus.Education.

Scott Miller

: Scott is responsible for the implementation of much of the cryptography
elements within Freenet.

Steven Starr

: Steven helps with administration of Freenet Project Inc, and is an advisor to
the project on business and publicity matters.

Dave Baker

: Dave's main contribution has been [Freemail](documentation.html#freemail),
his Summer of Code project to build a working email-over-Freenet system,
as well as some debugging and core work in various places.

Robert Hailey

: Robert has helped improve the speed and security of Freenet by finding two
**major** bugs, and has recently contributed some code.

David Sowder

: David (Zothar) has helped the Freenet Project as time permits and interest
directs, including configuration, statistics and peer management via FCP,
the FProxy stats page and Node 2 Node Messages (N2NM/N2NTMs).

And **hundreds of others**, who either haven't asked to be added here, who
prefer to remain nameless, or who we just haven't got around to thanking. Not to
mention thousands of users, testers, and [donors](donate.html#sponsors)!

### Papers

![][icon_pdf] [Measuring Freenet in the Wild: Censorship-resilience under Observation]({filename}/assets/papers/roos-pets2014.pdf) (PDF)
Observations and measurements on the live Freenet network. Includes suggestions
for improvement. This was submitted to PETS 2014.

![][icon_pdf] [The Dark Freenet]({filename}/assets/papers/freenet-0.7.5-paper.pdf) (PDF)
Detailed paper about the Freenet 0.7.5 network, as opposed to its routing
algorithm, which is detailed in the below papers. Includes some new
simulations. This has been submitted to PET 2010.

![][icon_video] [Video of Small World talk, Berlin, December 2005](http://player.vimeo.com/video/22488244?title=0&byline=0&portrait=0)  
This is a video of a talk given by Ian Clarke and Oskar Sandberg at the Chaos
Computer Congress in Berlin, December 2005, describing the (then) new
architecture for Freenet 0.7\. You can also download the [slideshow](
/assets/papers/ccc-slideshow.pdf.bz2), and the source for the Java [demo](
/assets/papers/ccc-freenet-demo.tar.bz2) (requires Java 1.5).

![][icon_pdf] [Searching in a Small World]({filename}/assets/papers/lic.pdf) (PDF)
Oskar Sandberg's licentiate thesis describing a simple decentralized
mechanism for constructing small world networks that is inspired by Freenet's
original design. Part II of the thesis describes the basis for the new
Darknet architecture.

![][icon_pdf] [Distributed routing in Small World Networks]({filename}/assets/papers/swroute.pdf) (PDF)
A paper by Oskar Sandberg describing the theoretical basis for the new
"Darknet" routing mechanism employed by Freenet 0.7.

![][icon_pdf] Chaos Computer Congress Talk (slideshow)  
This is a [slideshow]({filename}/assets/papers/ccc-slideshow.pdf.bz2) for a talk given
at the Chaos Computer Congress on 30th Dec 2005 in Berlin, Germany by Ian
Clarke and Oskar Sandberg. It described the new "darknet" approach to be
employed in Freenet 0.7\. A Java demonstration to accompany the talk is [
also]({filename}/assets/papers/ccc-freenet-demo.tar.bz2) available.

![][icon_pdf] [Switching for a small world]({filename}/assets/papers/vilhelm_thesis.pdf) (PDF)
A thesis by Vilhelm Verendel exploring ways to optimise the swapping algorithm.

![][icon_pdf] [Protecting Freedom of Information Online with Freenet]({filename}/assets/papers/freenet-ieee.pdf) (PDF)
An IEEE Internet Computing article describing the Freenet architecture circa
2002 - probably the best introduction to the theory behind Freenet.

![][icon_pdf] [FreeNet White Paper]({filename}/assets/papers/ddisrs.pdf) (PDF)
Original white paper by Ian Clarke, Division of Informatics, University of
Edinburgh 1999.

* * *

![][icon_pdf] [Attack Resistant Network Embeddings for Darknets](https://web.archive.org/web/20171210222609/https://www.ukp.tu-darmstadt.de/fileadmin/user_upload/Group_P2P/share/publications/Attack_Resistant_Network_Embeddings_for_Darknets.pdf) (PDF)  
A proposal for changing the darknet swapping algorithm which we are still
considering (we have some doubts about long-term performance).

![][icon_pdf] [A Contribution to Analyzing and Enhancing Darknet Routing](http://www.p2p.tu-darmstadt.de/publications/details/?no_cache=1&tx_bibtex_pi1%5Bpub_id%5D=TUD-CS-2013-0036) ([PDF](http://www.p2p.tu-darmstadt.de/fileadmin/user_upload/Group_P2P/share/INFOCOM.pdf))  
A proposal for changing the routing algorithm which we are still considering
(the worst case performance i.e. when a block has been lost may be
unacceptable).

![][icon_pdf] [Presentation: Towards "Dark" Social Networking Services (Strufe et al.)](https://www.icsi.berkeley.edu/icsi/sites/default/files/events/events_1303_strufe.pdf) (PDF)
An interesting presentation by the group responsible for the two above papers.

![][icon_pdf] [Pisces: Anonymous Communication Using Social Networks](http://arxiv.org/abs/1208.6326)  
An algorithm for setting up onion-like tunnels on darknets. 

![][icon_pdf] [Routing in the Dark: Pitch Black](http://grothoff.org/christian/pitchblack.pdf) ([citeseer](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.117.1543)) (PDF)  
A paper describing some attacks on Freenet 0.7's location swapping algorithm.
We have solutions for this but they are still being tested.

* * *

The most up to date reference is of course [the source code](
https://github.com/freenet/fred), but there is also some useful documentation on
[the wiki](https://wiki.freenetproject.org/) (you may have to search a bit),
and most implemented ideas have been discussed in detail on [the mailing
lists](help.html#mailing-lists) at some point, more recently often in-Freenet
forums such as FMS, or [the bug tracker](https://freenet.mantishub.io/) hosted by MantisHub.

[icon_pdf]: /assets/img/small-n-flat/file-pdf.png
[icon_video]: /assets/img/small-n-flat/file-video.png
