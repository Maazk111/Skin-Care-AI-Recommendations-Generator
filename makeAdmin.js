import prisma from "./prisma/prismaClient.js";

const makeAdmin = async (email) => {
  try {
    // Demote the current admin to a user
    await prisma.user.updateMany({
      where: { role: "ADMIN" },
      data: { role: "USER" },
    });

    // Promote the specified user to admin
    const user = await prisma.user.update({
      where: { email },
      data: { role: "ADMIN" },
    });

    console.log(`User ${user.email} is now an admin!`);
  } catch (error) {
    console.error("Error updating user role:", error);
  } finally {
    await prisma.$disconnect();
  }
};
// mmaazk111@gmail.com
// Call the function with the email of the user to promote
makeAdmin("zaryab@gmail.com");
