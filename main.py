import console_user_iterface
import game_logic


def main():
    field = game_logic.create_field()
    game_logic.do_step(field, 2, 0, False)
    game_logic.do_step(field, 1, 1, False)
    game_logic.do_step(field, 0, 2, False)
    # print(field)
    console_user_iterface.print_field(field)
    print(game_logic.check_win(field))


if __name__ == '__main__':
    main()
