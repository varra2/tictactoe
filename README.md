"# tictactoe" 

Код в файле ttt_game.py представляет реализацию игры в обратные крестики-нолики на поле 10 х 10, игра ведётся против компьютера. Приложение имеет командный интерфейс. Когда игрок или противник составляют ряд из пяти значков (учитываются горизонтальные, вертикальные, и диагональные ряды), игра заканчивается его поражением. При этом, при отображении игрового поля, сложившиеся в ряд значки будут заменены на "Z" (чтобы игроку легче было найти, где именно на поле он или противник потерпели поражение).

Чтобы начать игру, выберите, хотите ли вы играть за крестик или нолик. Для этого, введите "x" или "o" в английской раскладке, когда вопрос "Вы хотите играть за X или O?" появится на экране. Чтобы сделать ход, введите строку и столбец свободной ячейки, в которую хотите поставить свой значок. Например, чтобы сделать ход в клетку на строке E в столбце 2, введите "e2", когда предложение "Выберите свободную ячейку с A1 по J10: " появится на экране.

Если свободные ячейки закончатся, игра завершится ничьей.
В конце игры появится предложение начать игру заново: "Вы хотите продолжить игру? (y/n)" Чтобы согласиться, введите "y", "yes", "д" или "да", чтобы отказаться, введите "n", "no", "н" или "нет" (однобуквенные варианты на английском предложены в подсказке для удобства: так игроку не требуется переключать раскладку во время игры).

Код в файле display_board.py необходим для работы ttt_game.py (должен лежать в той же директории) и содержит инструкции по отрисовке игрового поля.