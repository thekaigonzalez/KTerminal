use strict;

use shared;
use Curses;
initscr;

sub printf
{
    my $newwstr  = join(' ', @_);
    Curses::printw($newwstr + "\n");
};
while (1) {

    Curses::printw("chroot\$runner-# ");

    my $str = getstring();
    my @args = split(" ", $str);
    my $command = $args[0];

    if ($command == "dir")
    {
        printw("you are inside chroot/home/runner/\n");
    }
    elsif ($command == "exit") {
        endwin();
    }
    else
    {
        printw("bash: invalid command\n");
    }
}

getchar;
endwin