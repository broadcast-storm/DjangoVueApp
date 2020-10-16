<template>
    <div class="navigation" :class="{ navigation_opened: opened }">
        <LogoSvg
            v-if="opened"
            class="navigation__logo"
            :regular-color="'#d8dcea'"
        />
        <div v-else class="navigation__logo"></div>
        <nav class="navigation__links-container">
            <ul class="navigation__links-list">
                <li
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
                        <span v-if="opened" class="link__text">{{
                            link.name
                        }}</span>
                    </router-link>
                </li>
            </ul>
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
            <span v-if="opened" class="exit-btn__text">Выход</span>
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
            opened: true,
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
        }
    },
    methods: {
        openMenu() {
            this.opened = !this.opened
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

    &_opened {
        width: 240px;
    }

    &__logo {
        height: 82px;
        margin: 0 auto 40px auto;
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
    }

    .open-btn {
        position: absolute;
        bottom: 30px;
        right: 30px;
        color: $basic-grey;
        cursor: pointer;

        &_opened {
            transform: rotate(180deg);
        }
    }
}
</style>
