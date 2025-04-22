# burgerbot
Burgerbot to jest bot do platformy [Twitch](https://twitch.tv/) z naciskiem na "minigry" tekstowe.

Korzystając z biblioteki [twitchio](https://pypi.org/project/twitchio/) łączy się z API Twitcha.
Projekt głównie opiera się na programowaniu obiektowym, dzieląc kod na oddzielne skrypty i obiekty dla elastyczniejszego i czystszego kodu.
Dla szybszego, prostszego i wygodniejszego tworzenia minigier, stworzony został obiekt GameManager dający szybki dostęp do wiadomości, stopera i sprawdzający stan każdej aktywnej rozgrywki, pozwalając dzięki temu mieć kilka rozgrywek aktywnych jednocześnie.
