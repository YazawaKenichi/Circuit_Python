//L チカ C 言語バージョン
//参考 https://note.com/rasen/n/n0dd582aa348c
//サイト内でも記述されているが、C での作成環境は公式 PDF を見るべし。
//(但し Ubuntu を想定している模様。)

#include "pico/stdlib.h"

int main()
{
    const uint LED_PIN = 25;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    while(1)
    {
        gpio_put(LED_PIN, 1);
        sleep_ms(50);
        gpio_put(LED_PIN, 0);
        sleep_ms(50);
    }
}
