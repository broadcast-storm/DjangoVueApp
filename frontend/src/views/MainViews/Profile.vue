<template>
    <div class="profile-wrapper">
        <div class="profile">
            <img src="" alt="User photo" class="profile__photo">
            <div class="profile-content">
                <h2 class="profile__name">{{ user.username }}</h2>
                <p class="profile__department">{{ user.department }}</p>
                <p class="profile__bio">{{ user.bio }}</p>
                <div class="profile__stats">
                    <div class="profile__stats-item">
                        <CoinSvg class="profile__stats-icon" />
                        <span class="profile__stats-value coins">{{ user.stats['coins'] }}</span>
                    </div>
                    <div class="profile__stats-item">
                        <LightningSvg class="profile__stats-icon" />
                        <span class="profile__stats-value lightnings">{{ user.stats['lightnings'] }}</span>
                    </div>
                    <div class="profile__stats-item">
                        <HeartSvg class="profile__stats-icon" />
                        <span class="profile__stats-value hearts">{{ user.stats['hearts'] }}</span>
                    </div>
                </div>
                <div class="profile__task">
                    <p class="profile__task-title">Основной квест:</p>
                    <h3 class="profile__task-name">{{ user.task.taskname }}</h3>
                    <ProgressBar :percent='user.task.progress' />
                    <p class="profile__task-deadline"><span>Срок:</span> до {{ date }}</p>
                </div>
                <table class="profile__props">
                    <tr class="profile__props-row">
                        <td class="profile__props-row-title">Продуктивность:</td>
                        <td class="profile__props-row-value">{{ user.productivity }}%</td>
                        <td class="profile__props-row-light">из 100% на сегодня</td>
                    </tr>
                    <tr class="profile__props-row">
                        <td class="profile__props-row-title">Качество:</td>
                        <td class="profile__props-row-value">{{ user.quality }}%</td>
                        <td class="profile__props-row-light">из 100 на сегодня</td>
                    </tr>
                    <tr class="profile__props-row">
                        <td class="profile__props-row-title">Текущий уровень:</td>
                        <td class="profile__props-row-value">{{ user.level }}%</td>
                        <td></td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import CoinSvg from '@/assets/icons/coin.svg'
import HeartSvg from '@/assets/icons/heart.svg'
import LightningSvg from '@/assets/icons/lightning.svg'
import ProgressBar from '@/components/ProgressBar.vue';
import { mapGetters } from 'vuex'

export default {
    name: 'Profile',
    components: {
        CoinSvg,
        HeartSvg,
        LightningSvg,
        ProgressBar
    },
    data() {
        return {
            user: Object.assign({}, this.$store.getters.getUserData)
        }
    },
    computed: {
        ...mapGetters(['getUserData']),
        date() {

            const date = this.getUserData.task.deadline;

            let month = date.getMonth() + 1;
            let days = date.getDate();
            month = month < 10 ? '0' + month : month;
            days = days < 10 ? '0' + days : days;

            return days + '.' + month + "." + date.getFullYear();
        }
    }
}

</script>

<style lang="scss" scoped>
.profile {
    background-color: #fff;
    box-sizing: border-box;
    width: calc(100% / 3);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 26px;
    padding-left: 39px;
    padding-bottom: 45px;
    padding-right: 21px;

    &__photo {
        width: 270px;
        height: 337px;
        border: 1px solid rgb(179, 179, 179);
        // To center alt 
        display: flex;
        justify-content: center;
        align-items: center;
    }

    &__name {
        font-size: 24px;
        text-align: center;
        font-weight: 400;
        line-height: 16px;
        color: $basic-black;
        margin-top: 22px;
    }

    &__department {
        color: $brand-gray-dark;
        margin-top: 16px;
        text-align: center;
    }

    &__bio {
        font-size: 18px;
        color: $brand-night;
        line-height: 20px;
        margin-top: 21px;
    }
}

.profile__stats {
    display: flex;
    width: 100%;
    justify-content: space-between;
    margin-top: 25px;
    flex-wrap: wrap;

    &-item {
        display: flex;
        align-items: center;
    }

    &-icon {
        width: 35px;
        height: 35px;
    }

    &-value {
        font-size: 18px;
        margin-left: 3px;
    }

    .coins {
        color: $text-color-yellow;
    }

    .lightnings {
        color: $text-color-green;
    }

    .hearts {
        color: $text-color-red;
    }
}

.profile__task {
    margin-top: 25px;
    display: flex;
    flex-direction: column;
    align-items: center;

    &-title {
        color: $basic-background;
        font-size: 18px;
        line-height: 16px;
        width: 100%;
    }

    &-name {
        font-size: 25px;
        color: $basic-black;
        line-height: 16px;
        margin: 0;
        margin-top: 8px;
        margin-bottom: 17px;
        width: 100%;
    }

    &-deadline {
        width: 100%;
        margin-top: 13px;
        color: $basic-black;
        font-size: 18px;
        line-height: 16px;

        span {
            color: $basic-background;
        }
    }
}

.profile__props {
    margin-top: 50px;
    display: flex;
    flex-direction: column;

    &-row {
        font-size: 18px;
        line-height: 16px;
        margin-top: 25px;

        &-title {
            width: 155px;
        }

        &-value {
            font-size: 24px;
            width: 60px;
        }

        &-light {
            font-size: 14px;
            line-height: 16px;
            color: $brand-gray-dark;
        }
    }

}

</style>