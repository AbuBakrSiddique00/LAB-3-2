// Using bit banding 
typedef unsigned int uint32_t;

/* Peripheral bit-band alias */
#define BITBAND_PERI_REF(addr, bit) \
    (*(volatile uint32_t *)(0x42000000U + \
    (((uint32_t)(addr) - 0x40000000U) * 32U) + \
    ((bit) * 4U)))

/* Register addresses */
#define RCC_APB2ENR_ADDR  0x40021018U
#define GPIOC_CRH_ADDR    0x40011004U
#define GPIOC_ODR_ADDR    0x4001100CU

/* Bit-band aliases */

/* RCC_APB2ENR bit 4 = IOPCEN */
#define GPIOC_CLOCK_EN \
    BITBAND_PERI_REF(RCC_APB2ENR_ADDR, 4)

/* GPIOC_CRH bits 20-23 configure PC13 */
#define PC13_MODE0 \
    BITBAND_PERI_REF(GPIOC_CRH_ADDR, 20)

#define PC13_MODE1 \
    BITBAND_PERI_REF(GPIOC_CRH_ADDR, 21)

#define PC13_MODE2 \
    BITBAND_PERI_REF(GPIOC_CRH_ADDR, 22)

#define PC13_MODE3 \
    BITBAND_PERI_REF(GPIOC_CRH_ADDR, 23)

/* GPIOC_ODR bit 13 = PC13 */
#define PC13 \
    BITBAND_PERI_REF(GPIOC_ODR_ADDR, 13)


void delay(volatile uint32_t count)
{
    while (count--);
}


int main(void)
{
    /* Enable GPIOC clock */
    GPIOC_CLOCK_EN = 1;

    /*
     * Configure PC13 as:
     *
     * MODE13 = 01  -> Output, 10 MHz
     * CNF13  = 00  -> General purpose push-pull
     *
     * CRH bits 23:20 = 0001
     */

    PC13_MODE0 = 1;
    PC13_MODE1 = 0;
    PC13_MODE2 = 0;
    PC13_MODE3 = 0;

    while (1)
    {
        /* PC13 LOW -> LED ON on typical Blue Pill */
        PC13 = 0;
        delay(500000);

        /* PC13 HIGH -> LED OFF */
        PC13 = 1;
        delay(5000000);
    }
}
