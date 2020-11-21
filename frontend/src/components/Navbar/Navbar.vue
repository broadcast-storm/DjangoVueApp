<template>
    <div class="navigation" :class="{ navigation_opened: opened }">
        <div class="navigation__logo-back" />
        <LogoSvg
            :class="{ navigation__logo_show: opened }"
            class="navigation__logo"
            :regular-color="'#d8dcea'"
        />

        <nav class="navigation__links-list">
            <div
                v-for="link in links"
                :key="link.name"
                class="navigation__links-item"
            >
                <router-link
                    :to="link.path"
                    class="link"
                    active-class="link_active"
                    exact
                >
                    <icon-base
                        :width="iconWidth"
                        :height="iconHeight"
                        :view-box-width="link.viewBoxWidth"
                        :view-box-height="link.viewBoxHeight"
                        :stroke-color="
                            link.strokeColor === null
                                ? 'currentColor'
                                : link.strokeColor
                        "
                        :fill-color="
                            link.fillColor === null
                                ? 'currentColor'
                                : link.fillColor
                        "
                        class="link__icon"
                    >
                        <component :is="link.icon"></component>
                    </icon-base>
                    <span
                        :class="{ 'show-text': showText }"
                        class="link__text"
                        >{{ link.name }}</span
                    >
                </router-link>
            </div>
        </nav>

        <nav class="navigation__links-list-mobile">
            <div
                v-for="linkMobile in linksMobile"
                :key="linkMobile.name"
                class="navigation__links-item"
            >
                <router-link
                    :to="linkMobile.path"
                    class="link"
                    active-class="link_active"
                    exact
                >
                    <icon-base
                        :width="iconWidthMobile"
                        :height="iconHeightMobile"
                        :view-box-width="linkMobile.viewBoxWidth"
                        :view-box-height="linkMobile.viewBoxHeight"
                        :stroke-color="
                            linkMobile.strokeColor === null
                                ? 'currentColor'
                                : linkMobile.strokeColor
                        "
                        :fill-color="
                            linkMobile.fillColor === null
                                ? 'currentColor'
                                : linkMobile.fillColor
                        "
                        class="link__icon"
                    >
                        <component :is="linkMobile.icon"></component>
                    </icon-base>
                </router-link>
            </div>
        </nav>

        <div class="exit-btn">
            <icon-base
                :width="25"
                :height="25"
                :view-box-width="26"
                :view-box-height="24"
                :stroke-color="'none'"
                class="exit-btn__icon"
            >
                <ExitSvg />
            </icon-base>
            <span class="exit-btn__text" :class="{ 'show-text': showText }"
                >Выход</span
            >
        </div>

        <icon-base
            :width="25"
            :height="25"
            :view-box-width="23"
            :view-box-height="21"
            :stroke-color="'none'"
            class="open-btn"
            :class="{ 'open-btn_opened': opened }"
            :on-click="openMenu"
        >
            <OpenSvg />
        </icon-base>
    </div>
</template>

<script>
import IconBase from './IconBase'
import CompetitionsSvg from './icons/CompetitionsSvg'
import ProfileSvg from './icons/ProfileSvg'
import MainQuestSvg from './icons/MainQuestSvg'
import StatisticsSvg from './icons/StatisticsSvg'
import RaitingSvg from './icons/RaitingSvg'
import ShopSvg from './icons/ShopSvg'
import TestsSvg from './icons/TestsSvg'
import ExitSvg from './icons/ExitSvg'
import OpenSvg from './icons/OpenSvg'

import LogoSvg from '@/components/LogoSvg'

import routesList from '@/router/routesList'

export default {
    components: {
        IconBase,
        CompetitionsSvg,
        ProfileSvg,
        MainQuestSvg,
        StatisticsSvg,
        RaitingSvg,
        ShopSvg,
        TestsSvg,
        ExitSvg,
        OpenSvg,
        LogoSvg,
    },
    data() {
        return {
            iconWidth: 25,
            iconHeight: 25,
            iconWidthMobile: 22,
            iconHeightMobile: 22,
            opened: false,
            showText: false,
            links: [
                {
                    path: routesList.mainPage.path,
                    icon: ProfileSvg,
                    name: 'Профиль',
                    viewBoxWidth: 19,
                    viewBoxHeight: 25,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.mainQuestPage.path,
                    icon: MainQuestSvg,
                    name: 'Основной квест',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.competitionsPage.path,
                    icon: CompetitionsSvg,
                    name: 'Соревнования',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.statisticsPage.path,
                    icon: StatisticsSvg,
                    name: 'Статистика',
                    viewBoxWidth: 25,
                    viewBoxHeight: 23,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.raitingPage.path,
                    icon: RaitingSvg,
                    name: 'Рейтинг',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.shopPage.path,
                    icon: ShopSvg,
                    name: 'Магазин',
                    viewBoxWidth: 24,
                    viewBoxHeight: 24,
                    strokeColor: null,
                    fillColor: 'none',
                },
                {
                    path: routesList.testsPage.path,
                    icon: TestsSvg,
                    name: 'Тесты',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
            ],
            linksMobile: [
                {
                    path: routesList.raitingPage.path,
                    icon: RaitingSvg,
                    name: 'Рейтинг',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.testsPage.path,
                    icon: TestsSvg,
                    name: 'Тесты',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.mainPage.path,
                    icon: ProfileSvg,
                    name: 'Профиль',
                    viewBoxWidth: 19,
                    viewBoxHeight: 25,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.mainQuestPage.path,
                    icon: MainQuestSvg,
                    name: 'Основной квест',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
                {
                    path: routesList.competitionsPage.path,
                    icon: CompetitionsSvg,
                    name: 'Соревнования',
                    viewBoxWidth: 18,
                    viewBoxHeight: 24,
                    strokeColor: 'none',
                    fillColor: null,
                },
            ],
        }
    },
    watch: {
        $route() {
            this.opened = false
            this.showText = false
        },
    },
    methods: {
        showTextFunc() {
            this.showText = true
        },
        openMenu() {
            this.opened = !this.opened
            if (this.showText) this.showText = false
            else {
                setTimeout(this.showTextFunc, 300)
            }
        },
    },
}
</script>

<style lang="scss" scoped>
.navigation {
    width: 80px;
    box-sizing: border-box;
    padding: 15px 0;
    background-color: $basic-background;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    transition: 0.3s width ease-in-out;

    &_opened {
        width: 240px;
    }

    &__logo {
        visibility: hidden;
        height: 82px;
        margin: 0 auto 40px auto;
        transition: 0.1s visibility ease-in-out;

        &_show {
            visibility: visible;
        }
    }

    &__links-list-mobile {
        display: none;
    }

    &__links-list {
        width: 100%;
    }

    &__links-item {
        box-sizing: border-box;
        list-style: none;
        width: 100%;
        margin-bottom: 25px;

        .link {
            box-sizing: border-box;
            width: 100%;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            color: $basic-grey;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 14px;
            padding: 5px 0 5px 20px;
            border-left: 5px solid transparent;
            &__icon {
                margin-right: 20px;
            }

            &_active {
                color: white;
                border-left: 5px solid white;
                padding-left: -5px;
            }
            &__text {
                display: none;
            }
        }
        .link:hover {
            color: white;
        }
    }

    .exit-btn {
        margin-top: 70px;
        box-sizing: border-box;
        width: 100%;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        color: $brand-night;
        text-decoration: none;
        text-transform: uppercase;
        font-size: 14px;
        padding: 5px 0 5px 20px;
        border-left: 5px solid transparent;
        cursor: pointer;
        &__icon {
            margin-right: 20px;
        }
        &__text {
            display: none;
        }
    }

    .open-btn {
        position: absolute;
        bottom: 30px;
        right: 30px;
        color: $basic-grey;
        cursor: pointer;

        transition: 0.3s transform ease-in-out;

        &_opened {
            transform: rotate(180deg);
        }
    }
    .open-btn:hover {
        color: white;
    }
    .show-text {
        display: inline;
    }
}

@media (max-width: $media-breakpoint-sm) {
    .navigation {
        top: auto;
        bottom: 0;
        width: 100%;
        height: 56px;
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 0;
        background-color: $basic-grey;
        box-shadow: 0px -2px 4px rgba(0, 0, 0, 0.1);

        &__logo,
        &__logo-back,
        &__links-list,
        .open-btn,
        .exit-btn {
            display: none;
        }

        &__links-list-mobile {
            display: flex;
            justify-content: space-around;
            width: 100%;
        }

        &__links-item {
            box-sizing: border-box;
            margin-bottom: 0;
            width: 40px;
            height: 40px;
            left: calc(50% - 36px / 2 - 144px);
            bottom: 10px;
            box-shadow: -4px -4px 7px rgba(255, 255, 255, 0.35),
                4px 4px 7px rgba(0, 0, 0, 0.15),
                inset -4px -4px 4px rgba(255, 255, 255, 0.05),
                inset 2px 2px 4px rgba(0, 0, 0, 0.05);
            border-radius: 15px;
            display: flex;
            justify-content: center;
            align-items: center;

            .link {
                width: 25px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: $basic-background;
                padding: 0;
                border: none;
                -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
                &__icon {
                    margin-right: 0;
                }
                &__text {
                    display: none;
                }

                &_active {
                    color: $brand-turquoise;
                }
            }
            .link:hover {
                color: $brand-turquoise;
            }
        }
    }
}
</style>
