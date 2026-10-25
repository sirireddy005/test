
function getUser(user) {
    return user.profile.name;
}

console.log(getUser(null));

module.exports = getUser;
