<template>
    <div class="profile-wrapper">
        <div class="profile">
            <img src="" alt="Uesr photo" class="profile__photo">
            <h2 class="profile__name">{{ user.username }}</h2>
            <p class="profile__department">{{ user.department }}</p>
            <p class="bio">{{ user.bio }}</p>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'Profile',
    props: {},
    data: {
        user: this.getUserData
    },
    computed: {
        ...mapGetters(['getUserData'])
    },
}
</script>

<style lang="scss" scoped></style>