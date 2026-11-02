typedef unsigned int uint32_t;

#define RCC_APB2ENR (*(volatile uint32_t *)0x40021018)

#define GPIOC_CRH   (*(volatile uint32_t *)0x40011004)
#define GPIOC_BSRR  (*(volatile uint32_t *)0x40011010)
#define GPIOC_BRR   (*(volatile uint32_t *)0x40011014)

void delay(volatile uint32_t count)
{
    while (count--);
}

int main(void)
{
    RCC_APB2ENR |= (1U << 4);

    GPIOC_CRH &= ~(0xFU << 20);
    GPIOC_CRH |=  (0x1U << 20);

    while (1)
    {
        GPIOC_BRR = (1U << 13);
        delay(500000);

        GPIOC_BSRR = (1U << 13);
        delay(5000000);
    }
}


